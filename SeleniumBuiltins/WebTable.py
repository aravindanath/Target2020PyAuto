

from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
lp.driver.get("https://www.redbus.in/")





time.sleep(5)
lp.driver.quit()



