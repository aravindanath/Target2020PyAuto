
from configparser import ConfigParser
from selenium. webdriver import Chrome
from selenium.webdriver.common.keys import Keys

config =  ConfigParser()
configFile = "../testdata/data.ini"
config.add_section("Tc004")
config.set("Tc004","user","arvind")
with open(configFile,'a') as t:
    config.write(t)

