from os import environ, path
import os
import configparser
#from dotenv import load_dotenv

def init_setup():
    basedir = path.abspath(os.getcwd())
    #load_dotenv(path.join(basedir, '.env'))

    os.environ['BASEPATH'] = basedir

    # Read local `config.ini` file.
    config = configparser.ConfigParser()   
    config.read('settings/settings.ini')
    config.read(os.path.join(basedir, 'settings.ini'))

    for section in config.sections():
        for key, value in config.items(section):
            os.environ[section+'_'+key] = value
            
    

