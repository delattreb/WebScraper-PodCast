# coding=utf-8
"""
scrapperFranceInter.py v1.1.0
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

import os.path
import urllib.request

import requests
from bs4 import BeautifulSoup

from lib import com_config, com_email, com_logger, com_sqlite, fileutils


class FranceInter:
    def __init__(self):
        conf = com_config.Config()
        self.config = conf.getconfig()
        self.fileutils = fileutils.FileUtils()
        
    def scrap(self):
        logger = com_logger.Logger('France Inter')
        
        table = []
        for conf in self.config['URLFRANCEINTER']:
            url = self.config['URLFRANCEINTER'][str(conf)]
            logger.info('Check URL:' + url)
            if requests.get(url).status_code == 200:
                url = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(url, "html.parser")
                soup.prettify()
                
                div_list = soup.find("div", class_ = "diffusions-list")
                for article_list in div_list.find_all("article", class_ = "rich-section-list-item "):
                    try:
                        a_link = article_list.find("button", class_ = "replay-button playable")["data-url"]
                        a_name = article_list.find("a", class_ = "rich-section-list-item-content-title")["title"]
                        a_name += ' ' + article_list.find("span", class_ = "rich-section-list-item-content-infos-date").text
                        a_name = self.fileutils.replace(a_name)
                        
                        logger.debug('Find: ' + a_name)
                        if com_sqlite.select(a_name) != a_name:
                            base_dir = os.path.dirname(os.path.abspath(__file__))
                            db_path = os.path.join(base_dir, self.config['DIRDOWNLOAD']['DIR'])
                            urllib.request.urlretrieve(a_link, db_path + "/" + a_name + ".mp3")
                            logger.info('Downloaded: ' + a_name)
                            com_sqlite.insert(a_name)
                            table.append(a_name)
                            mail = com_email.Mail()
                            mail.send_mail_gmail("France Inter: " + a_name, table)
                    except Exception as exp:
                        logger.error(repr(exp))
                    break
