
from configparser import ConfigParser
from selenium. webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from pyjavaproperties import Properties
from faker import Faker


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

def getValue(key,path):
    prop =Properties()
    file =open(path,'r')
    prop.load(file)
    return prop.getProperty(key)

def generateEmail():
    fake =  Faker()
    val =fake.name()
    return str(val).replace(" ","").replace(".","")+"@testmail.com"

def generateFirstName():
    fake =  Faker()
    val =fake.name()
    return str(val).replace(".","").split(" ")[0]

def generateLastName():
    fake =  Faker()
    val =fake.name()
    return str(val).split(" ")[1]
