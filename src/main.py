# coding=utf-8
"""
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

import scraperBBC
import scraperFranceInter
import scapperRTL
from lib import com_logger, com_config

com_config.setConfig()
config = com_config.getConfig()
logger = com_logger.Logger('Main')

logger.info(config['APPLICATION']['name'] + ' ' + config['APPLICATION']['version'])
logger.info('Start')

scapperRTL.RTL()
scraperFranceInter.FranceInter()
scraperBBC.BBC4Science()

logger.info('Stop')
