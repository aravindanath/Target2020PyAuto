from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys


lp.driver.get("https://www.google.com")

# //*[@name='q']--> * ALL the elements
lp.driver.find_element_by_xpath("//input[@name='q']").send_keys("Relative xpath")


time.sleep(3)
lp.driver.quit()