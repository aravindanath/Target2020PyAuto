from pyjavaproperties import Properties
from Day6 import BaseClass as bc
from selenium. webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
path ="../config.properties"

driver = Chrome("../driver/chromedriver")
driver.fullscreen_window()
driver.get(bc.getValue("url",path))
driver.find_element_by_name("q").send_keys(bc.getValue("search",path),Keys.ENTER)
time.sleep(3)
driver.quit()