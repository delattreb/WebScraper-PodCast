# coding=utf-8
"""
scrapper.py v1.1.0
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

import os.path
import urllib.request

import requests
from bs4 import BeautifulSoup

from lib import com_config, com_email, com_sqlite, com_logger


class BBC4Science:
    def __init__(self):
        config = com_config.getConfig()
        logger = com_logger.Logger('BBC')
        
        for conf in config['URLBBC']:
            url = config['URLBBC'][str(conf)]
            logger.info('Check URL: ' + url)
            if requests.get(url).status_code == 200:
                url = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(url, "html.parser")
                soup.prettify()
                
                ul_list = soup.find_all("ul", class_="list-unstyled")
                for div_list in soup.find_all("div", class_="block-link__link programme__favourites centi"):
                    a_link = div_list.find("a", class_="link-complex br-linkinvert buttons__download__link")["href"]
                    a_name = div_list.find("a", class_="link-complex br-linkinvert buttons__download__link")["download"].replace("'", "").replace('"', "").replace(
                        ':', "").replace('?', "")
                    logger.debug('Find: ' + a_name)
                    if com_sqlite.select(a_name) != a_name:
                        base_dir = os.path.dirname(os.path.abspath(__file__))
                        db_path = os.path.join(base_dir, config['DIRDOWNLOAD']['DIR'])
                        urllib.request.urlretrieve(a_link, db_path + "/" + a_name)
                        logger.info('Downloaded: ' + a_name)
                        com_sqlite.insert(a_name)
                        table = []
                        table.append(a_name)
                        com_email.send_mail_gmail("PodCast: " + a_name, table)
                    break
