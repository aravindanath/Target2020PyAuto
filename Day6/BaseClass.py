
from configparser import ConfigParser
from selenium. webdriver import Chrome
from selenium.webdriver.common.keys import Keys


def writeINI(path,mode,header,key,value):
    config =  ConfigParser()
    config.add_section(header)
    config.set(header,key,value)
    with open(path,mode) as t:
        config.write(t)

def readINI(path,header,key):
    config = ConfigParser()
    config.read(path)
    value = config.get(header,key)
    return value
