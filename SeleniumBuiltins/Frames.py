

from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
lp.driver.get("https://docs.oracle.com/javase/7/docs/api/")


lp.driver.switch_to.frame("packageListFrame")
print("Switch sucess")
lp.driver.find_element_by_link_text("java.awt.color").click()
time.sleep(2)

lp.driver.switch_to.default_content()
lp.driver.switch_to.frame("packageFrame")
lp.driver.find_element_by_link_text("ColorSpace").click()
time.sleep(2)

lp.driver.switch_to.default_content()
lp.driver.switch_to.frame("classFrame")
lp.driver.find_element_by_link_text("java.lang.Object")





time.sleep(2)
lp.driver.quit()



