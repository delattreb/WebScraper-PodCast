import glob
import os
import os.path
import shutil


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
