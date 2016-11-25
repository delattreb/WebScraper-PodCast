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

from lib import com_config, com_email, com_sqlite, com_logger


class FranceInter:
    def __init__(self):
        config = com_config.getConfig()
        logger = com_logger.Logger('France Inter')
        
        for conf in config['URLFRANCEINTER']:
            url = config['URLFRANCEINTER'][str(conf)]
            logger.info('Check URL:' + url)
            if requests.get(url).status_code == 200:
                url = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(url, "html.parser")
                soup.prettify()
                
                div_list = soup.find("div", class_="diffusions-list")
                for article_list in div_list.find_all("article", class_="rich-section-list-item "):
                    try:
                        a_link = article_list.find("button", class_="replay-button playable")["data-url"]
                        a_name = article_list.find("a", class_="rich-section-list-item-content-title")["title"].replace("'", "").replace('"', "").replace(':',
                                                                                                                                                          "").replace(
                            '?', "")
                        a_name += ' ' + article_list.find("span", class_="rich-section-list-item-content-infos-date").text.replace('û', 'u').replace('ê', 'e')
                        logger.debug('Find: ' + a_name)
                        if com_sqlite.select(a_name) != a_name:
                            base_dir = os.path.dirname(os.path.abspath(__file__))
                            db_path = os.path.join(base_dir, config['DIRDOWNLOAD']['DIR'])
                            urllib.request.urlretrieve(a_link, db_path + "/" + a_name + ".mp3")
                            logger.info('Downloaded: ' + a_name)
                            com_sqlite.insert(a_name)
                            table = []
                            table.append(a_name)
                            com_email.send_mail_gmail("PodCast: " + a_name, table)
                    except:
                        logger.error('Name: ' + a_name)
                    break
