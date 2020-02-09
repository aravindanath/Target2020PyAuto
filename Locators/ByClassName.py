from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys


lp.driver.get("https://www.icicibank.com")

lp.driver.find_element_by_class_name("pl-login-ornage-box").click()

time.sleep(3)
lp.driver.quit()
