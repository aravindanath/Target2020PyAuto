

from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.action_chains import ActionChains
lp.driver.get("http://the-internet.herokuapp.com/drag_and_drop")


src =lp.driver.find_element_by_css_selector("#column-a")
dec = lp.driver.find_element_by_css_selector("#column-b")

time.sleep(2)
act =ActionChains(lp.driver)
time.sleep(2)
act.drag_and_drop(src,dec).perform();

# time.sleep(3)

# lp.driver.quit()



