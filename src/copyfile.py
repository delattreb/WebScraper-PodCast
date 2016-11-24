# coding=utf-8

from lib import fileutils
from lib import com_config
import os.path


print("Start")
config = com_config.getConfig()
sourcepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), config['DIRDOWNLOAD']['DIR'])
destpath = config['DIRCOPY']['DIR']
fileutils.movelist(sourcepath, destpath)
print("End")

