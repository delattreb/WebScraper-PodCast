# coding=utf-8

import os.path

from lib import com_config, fileutils

print("Start")
conf = com_config.Config()
config = conf.getconfig()
sourcepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), config['DIRDOWNLOAD']['DIR'])
destpath = config['DIRCOPY']['DIR']

fileutil = fileutils.FileUtils()
fileutil.movelist(sourcepath, destpath)
print("End")
