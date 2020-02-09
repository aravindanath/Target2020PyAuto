
from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.google.com")
lp.driver.find_element_by_xpath("//input[starts-with(@class,'gL')]").send_keys("Selenium jobs 2020",Keys.ENTER)
time.sleep(3)#

lp.driver.quit()