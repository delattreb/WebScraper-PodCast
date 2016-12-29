"""
com_config.py v1.3.0
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import configparser
import os.path

config_file = "config/config.ini"


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.configraw = configparser.RawConfigParser()
    
    def setconfig(self):
        # Version
        self.config['APPLICATION'] = {}
        self.config['APPLICATION']['name'] = 'Web Scrapper'
        self.config['APPLICATION']['version'] = '1.4.0'
        self.config['APPLICATION']['author'] = 'Bruno DELATTRE'
        
        # LOGGER
        self.config['LOGGER'] = {}
        self.config['LOGGER']['levelconsole'] = '10'  # DEBUG=10 INFO=20 WARNING=30 ERROR=40 #CRITICAL=50
        self.config['LOGGER']['levelfile'] = '40'
        self.config['LOGGER']['logfile'] = 'log'
        self.config['LOGGER']['logfilesize'] = '1000000'
        
        # EMAIL
        self.config['EMAIL'] = {}
        self.config['EMAIL']['from'] = 'pythonuseriot@gmail.com'
        self.config['EMAIL']['to'] = 'delattreb@gmail.com'
        self.config['EMAIL']['password'] = 'pythonuser'
        
        # SQLite
        self.config['SQLITE'] = {}
        self.config['SQLITE']['database'] = 'database.db'
        
        # URL RTL
        self.config['URLRTL'] = {}
        self.config['URLRTL']['1'] = 'http://www.rtl.fr/emission/laurent-gerra'
        self.config['URLRTL']['2'] = 'http://www.rtl.fr/emission/c-est-a-lire'
        
        # URL BBC
        self.config['URLBBC'] = {}
        self.config['URLBBC']['1'] = 'http://www.bbc.co.uk/programmes/p02nrxgq/episodes/downloads'
        self.config['URLBBC']['2'] = 'http://www.bbc.co.uk/programmes/b036f7w2/episodes/downloads'
        self.config['URLBBC']['3'] = 'http://www.bbc.co.uk/programmes/b019dl1b/episodes/downloads'
        self.config['URLBBC']['4'] = 'http://www.bbc.co.uk/programmes/b006s7d6/episodes/downloads'
        self.config['URLBBC']['5'] = 'http://www.bbc.co.uk/programmes/b006qng8/episodes/downloads'
        self.config['URLBBC']['6'] = 'http://www.bbc.co.uk/programmes/b01jxzy9/episodes/downloads'
        self.config['URLBBC']['7'] = 'http://www.bbc.co.uk/programmes/b04gyx0t/episodes/downloads'
        
        # URL FRANCE INTER
        self.config['URLFRANCEINTER'] = {}
        self.config['URLFRANCEINTER']['1'] = 'https://www.franceinter.fr/emissions/la-tete-au-carre'
        self.config['URLFRANCEINTER']['2'] = 'https://www.franceinter.fr/emissions/affaires-sensibles'
        
        # Directory Download
        self.config['DIRDOWNLOAD'] = {}
        self.config['DIRDOWNLOAD']['DIR'] = 'download'
        
        # Directory Coppy
        self.config['DIRCOPY'] = {}
        self.config['DIRCOPY']['DIR'] = '/volumeUSB1/usbshare'
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, config_file)
        with open(db_path, 'w') as configfile:
            self.config.write(configfile)
    
    def getconfig(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, config_file)
        self.configraw.read(db_path)
        return self.configraw
