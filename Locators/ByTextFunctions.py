
from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.facebook.com")
lp.driver.find_element_by_xpath("(//button[text()='Sign Up' and starts-with(@id,'u_0')])[1]").click()
time.sleep(3)

lp.driver.quit()