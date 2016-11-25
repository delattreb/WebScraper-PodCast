# coding=utf-8
"""
scrapperRTL.py v1.1.0
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

import os.path
import urllib.request

import requests
from bs4 import BeautifulSoup

from lib import com_config, com_email, com_sqlite, com_logger


class RTL:
    def __init__(self):
        config = com_config.getConfig()
        logger = com_logger.Logger('RTL')
        
        for conf in config['URLRTL']:
            url = config['URLRTL'][str(conf)]
            logger.info('Check URL: ' + url)
            if requests.get(url).status_code == 200:
                url = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(url, "html.parser")
                soup.prettify()
                
                for div_list in soup.find_all("div", class_="timeline-post shift"):
                    a_name = ''
                    try:
                        div_item = div_list.find("div", class_="post-fig brd brd-grey")
                        a_link = div_item.find("a", class_="post-link")["href"]
                        
                        if requests.get(a_link).status_code == 200:
                            a_link = urllib.request.urlopen(a_link).read()
                            soupnext = BeautifulSoup(a_link, "html.parser")
                            soupnext.prettify()
                            div_mp3 = soupnext.find("figcaption", class_="figcaption article-mdl cf")
                            a_name = div_mp3.find("span", class_="legend").text.replace("'", "").replace('"', "").replace(
                                ':', "").replace('?', "")
                            
                            a_link = div_mp3.find("a", class_="dl icon icon-download")["href"]
                            
                            logger.debug('Find: ' + a_name)
                            if com_sqlite.select(a_name) != a_name:
                                base_name = os.path.dirname(os.path.abspath(__file__))
                                db_path = os.path.join(base_name, config['DIRDOWNLOAD']['DIR'])
                                urllib.request.urlretrieve(a_link, db_path + "/" + a_name + ".mp3")
                                logger.info('Downloaded: ' + a_name)
                                com_sqlite.insert(a_name)
                                table = []
                                table.append(a_name)
                                com_email.send_mail_gmail("PodCast: " + a_name, table)
                            break
                    except:
                        logger.error('Name: ' + a_name)
