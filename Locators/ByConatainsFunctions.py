
from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.flipkart.com")
lp.driver.find_element_by_xpath("//*[text()='✕' or text()='X']").click()
time.sleep(3)
lp.driver.get("https://www.hdfcbank.com/")
try:

    lp.driver.find_element_by_xpath("//*[text()='✕' or text()='X']").click()
except:
    print("Not found")

time.sleep(3)


lp.driver.quit()