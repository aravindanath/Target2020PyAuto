from browserLaunch import launchChrome as op
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://www.amazon.com")
op.driver.find_element_by_id("twotabsearchtextbox").send_keys("Womens wrist watch",Keys.ENTER)


time.sleep(3)
op.driver.quit()