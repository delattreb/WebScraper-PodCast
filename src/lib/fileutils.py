import glob
import os
import os.path
import shutil


class FileUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def replace(val):
        dico_car_part = {'\\': '',
                         ':':  ' ',
                         '%':  '',
                         '*':  '',
                         '"':  ' ',
                         '\'': ' ',
                         '’': ' ',
                         '!':  '',
                         ',':  ' ',
                         '-':  ' ',
                         '?':  ''
                         }
        result = val
        for cle, valeur in dico_car_part.items():
            result = result.replace(cle, valeur)
        return result
    
    @staticmethod
    def movelist(sourcepath, destpath):
        try:
            os.chdir(sourcepath)
            if os.path.exists(destpath):
                print('Moving files...')
                for file in glob.glob("*.*"):
                    print('Moving: ' + sourcepath + "/" + file)
                    shutil.move(sourcepath + "/" + file, destpath + "/" + file)
            else:
                print('Destination not preset')
        except:
            pass
