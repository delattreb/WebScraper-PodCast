# coding=utf-8
"""
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

import scapperRTL
import scraperBBC
import scraperFranceInter
from lib import com_config, com_logger

conf = com_config.Config()
conf.setconfig()
config = conf.getconfig()

logger = com_logger.Logger('Main')
logger.info(config['APPLICATION']['name'] + ' ' + config['APPLICATION']['version'])
logger.info('Start')

# Scrap !   INFO: soup.findall(attrs={'class':None or value})
bbc = scraperBBC.BBC()
bbc.scrap()

rtl = scapperRTL.RTL()
rtl.scrap()

fi = scraperFranceInter.FranceInter()
fi.scrap()

logger.info('Stop')
