from os import environ, path
import os
import configparser

def init_setup():
    basedir = path.abspath(os.getcwd())

    os.environ['BASEPATH'] = basedir

    # Read local `config.ini` file.
    config = configparser.ConfigParser()   
    config.read('settings/settings.ini')
    config.read(os.path.join(basedir, 'settings.ini'))

    # store all config variables in environment variables
    for section in config.sections():
        for key, value in config.items(section):
            os.environ[section+'_'+key] = value
            
    

