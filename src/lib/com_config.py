"""
com_config.py v1.0.0
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import configparser
import os.path

config_file = "config/config.ini"


def setConfig():
    config = configparser.ConfigParser()
    
    # Version
    config['APPLICATION'] = {}
    config['APPLICATION']['name'] = 'Web Scrapper'
    config['APPLICATION']['version'] = '1.2.0'
    config['APPLICATION']['author'] = 'Bruno DELATTRE'
    
    # LOGGER
    config['LOGGER'] = {}
    config['LOGGER']['levelconsole'] = '10'  # DEBUG=10 INFO=20 WARNING=30 ERROR=40 #CRITICAL=50
    config['LOGGER']['levelfile'] = '40'
    config['LOGGER']['logfile'] = 'log'
    config['LOGGER']['logfilesize'] = '1000000'
    
    # EMAIL
    config['EMAIL'] = {}
    config['EMAIL']['from'] = 'pythonuseriot@gmail.com'
    config['EMAIL']['to'] = 'delattreb@gmail.com'
    config['EMAIL']['password'] = 'pythonuser'
    
    # SQLite
    config['SQLITE'] = {}
    config['SQLITE']['database'] = 'database.db'
    
    # URL RTL
    config['URLRTL'] = {}
    config['URLRTL']['1'] = 'http://www.rtl.fr/emission/laurent-gerra'
    config['URLRTL']['2'] = 'http://www.rtl.fr/emission/c-est-a-lire'
    
    # URL BBC
    config['URLBBC'] = {}
    config['URLBBC']['1'] = 'http://www.bbc.co.uk/programmes/p02nrxgq/episodes/downloads'
    config['URLBBC']['2'] = 'http://www.bbc.co.uk/programmes/b036f7w2/episodes/downloads'
    config['URLBBC']['3'] = 'http://www.bbc.co.uk/programmes/b019dl1b/episodes/downloads'
    config['URLBBC']['4'] = 'http://www.bbc.co.uk/programmes/b006s7d6/episodes/downloads'
    config['URLBBC']['5'] = 'http://www.bbc.co.uk/programmes/b006qng8/episodes/downloads'
    config['URLBBC']['6'] = 'http://www.bbc.co.uk/programmes/b01jxzy9/episodes/downloads'
    config['URLBBC']['7'] = 'http://www.bbc.co.uk/programmes/b04gyx0t/episodes/downloads'
    
    # URL FRANCE INTER
    config['URLFRANCEINTER'] = {}
    config['URLFRANCEINTER']['1'] = 'https://www.franceinter.fr/emissions/la-tete-au-carre'
    config['URLFRANCEINTER']['2'] = 'https://www.franceinter.fr/emissions/rendez-vous-avec-x'
    
    # Directory Download
    config['DIRDOWNLOAD'] = {}
    config['DIRDOWNLOAD']['DIR'] = 'download'
    
    # Directory Coppy
    config['DIRCOPY'] = {}
    config['DIRCOPY']['DIR'] = '/volumeUSB1/usbshare'
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, config_file)
    with open(db_path, 'w') as configfile:
        config.write(configfile)


def getConfig():
    config = configparser.RawConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, config_file)
    config.read(db_path)
    return config
