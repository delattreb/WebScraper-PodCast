# coding=utf-8
"""
scrapper.py v1.2.0
Auteur: Bruno DELATTRE
Date : 12/08/2016

New version: download High quality
"""

import os.path
import urllib.request

import requests
from bs4 import BeautifulSoup

from lib import com_config, com_email, com_logger, com_sqlite, fileutils


class BBC:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        self.fileutils = fileutils.FileUtils()
    
    def scrap(self):
        logger = com_logger.Logger('BBC')
        
        table = []
        try:
            for conf in self.config['URLBBC']:
                url = self.config['URLBBC'][str(conf)]
                logger.info('Check URL: ' + url)
                if requests.get(url).status_code == 200:
                    url = urllib.request.urlopen(url).read()
                    soup = BeautifulSoup(url, "html.parser")
                    soup.prettify()
                    
                    for ul_list in soup.find_all("ul", class_ = "list-unstyled"):
                        div_test = ul_list.find_all("div", class_ = "programme__body")
                        if len(div_test) > 0:
                            for li_list in ul_list.find_all("li", class_ = ""):
                                for div_list in li_list.find_all("div", class_ = "programme__body"):
                                    span_name = div_list.find("span", class_ = "programme__title ")
                                    a_name = self.fileutils.replace(span_name.find("span").text)
                                    
                                    div_link = div_list.find("div", class_ = "popup__content popup__content--download br-box-subtle br-subtle-link-onbg br-subtle-link-onborder")
                                    if div_link is not None:
                                        a_link = div_link.find("a", class_ = "link-complex popup__list__item island--squashed br-subtle-bg-ontext br-subtle-bg-onbg--hover br-subtle-link-ontext--hover")["href"]
                                        
                                        logger.debug('Find: ' + a_name)
                                        if com_sqlite.select(a_name) != a_name:
                                            base_dir = os.path.dirname(os.path.abspath(__file__))
                                            db_path = os.path.join(base_dir, self.config['DIRDOWNLOAD']['DIR'])
                                            urllib.request.urlretrieve(a_link, db_path + "/" + a_name + ".mp3")
                                            logger.info('Downloaded: ' + a_name + ".mp3")
                                            com_sqlite.insert(a_name)
                                            table.append(a_name)
                                            mail = com_email.Mail()
                                            mail.send_mail_gmail("BBC: " + a_name, table)
                                break
        except Exception as exp:
            logger.error(repr(exp))
