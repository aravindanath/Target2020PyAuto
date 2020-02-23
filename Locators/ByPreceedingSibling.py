from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("http://the-internet.herokuapp.com/tables")




web = lp.driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td[contains(text(),'Tim')]//preceding-sibling::td").text

print("last name ",web)


time.sleep(3)
lp.driver.close()