from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys


lp.driver.get("https://www.google.com")

lp.driver.find_element_by_name("q").send_keys("New year partys in bangalore",Keys.ENTER)

time.sleep(3)
lp.driver.quit()
