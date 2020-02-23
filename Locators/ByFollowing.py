from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("http://the-internet.herokuapp.com/tables")


fName = "//table[@id='table1']/tbody/tr/td[contains(text(),'FIRSTNAME')]//following::td[3]".replace("FIRSTNAME","Frank")

web = lp.driver.find_element_by_xpath(fName).text

print("Website ",web)


time.sleep(3)
lp.driver.close()