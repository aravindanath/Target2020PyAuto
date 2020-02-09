from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys


lp.driver.get("https://www.google.com")

lp.driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div/div/div/div[2]/input").send_keys("xapths")

time.sleep(3)
lp.driver.quit()