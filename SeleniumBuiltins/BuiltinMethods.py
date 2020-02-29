from browserLaunch import launchChrome as lp
from selenium.webdriver.common.keys import Keys
import time

lp.driver.get("https://www.google.com")

lp.driver.find_element_by_name("q").send_keys("selenium jobs",Keys.ENTER)

time.sleep(2)
lp.driver.refresh()
time.sleep(2)
lp.driver.back()
lp.driver.refresh()
time.sleep(2)
lp.driver.forward()
lp.driver.close()
