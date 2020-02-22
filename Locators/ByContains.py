from browserLaunch import launchChrome as op
import time
from selenium.webdriver.common.keys import Keys



op.driver.get("https://www.amazon.com")
time.sleep(2)
op.driver.find_element_by_xpath("//span[contains(text(),'Hello.') or contains(text(),'Hello,')]").click()
time.sleep(2)
op.driver.get("https://www.amazon.in")
op.driver.find_element_by_xpath("//span[contains(text(),'Hello.') or contains(text(),'Hello,')]").click()
time.sleep(2)

op.driver.quit()
