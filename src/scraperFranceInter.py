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
    
    def scrapxml(self):
        logger = com_logger.Logger('France Inter')
        
        table = []
        for conf in self.config['URLFRANCEINTER']:
            url = self.config['URLFRANCEINTER'][str(conf)]
            logger.info('Check URL:' + url)
            if requests.get(url).status_code == 200:
                url = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(url, "lxml")
                soup.prettify()
                
                for item_list in soup.find_all("item"):
                    a_name = self.fileutils.replace(item_list.find("title").text)
                    a_link = item_list.find("guid").text
                    
                    logger.info('Find: ' + a_name)
                    if com_sqlite.select(a_name) != a_name:
                        base_dir = os.path.dirname(os.path.abspath(__file__))
                        db_path = os.path.join(base_dir, self.config['DIRDOWNLOAD']['DIR'])
                        urllib.request.urlretrieve(a_link, db_path + "/" + a_name + ".mp3")
                        logger.info('Downloaded: ' + a_name)
                        com_sqlite.insert(a_name)
                        table.append(a_name)
                        mail = com_email.Mail()
                        mail.send_mail_gmail("France Inter: " + a_name, table)
                    break
