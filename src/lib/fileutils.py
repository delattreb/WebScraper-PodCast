import glob
import os
import os.path
import shutil

from lib import com_logger


class FileUtils:
    def __init__(self):
        self.logger = com_logger.Logger('FILE')
    
    @staticmethod
    def replace(val):
        dico_car_part = {'\\': '',
                         ':':  ' ',
                         '%':  '',
                         '*':  '',
                         '"':  ' ',
                         '\'': '',
                         '/':  '',
                         '’':  ' ',
                         '!':  '',
                         ',':  '',
                         ';':  '',
                         '-':  ' ',
                         '?':  ''
                         }
        result = val
        for cle, valeur in dico_car_part.items():
            result = result.replace(cle, valeur)
        return result
    
    def movelist(self, sourcepath, destpath):
        try:
            os.chdir(sourcepath)
            if os.path.exists(destpath):
                print('Moving files...')
                for file in glob.glob("*.*"):
                    print('Moving: ' + sourcepath + "/" + file)
                    shutil.move(sourcepath + "/" + file, destpath + "/" + file)
            else:
                print('Destination not preset')
        except Exception as exp:
            self.logger.error(str(exp))
