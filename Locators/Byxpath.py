from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys


"""
Abs xpath = /html/body/div/div[4]/form/div[2]/div/div/div/div[2]/input

Relative xpath = //input[@name='q']
AND OR
//TAGNAME[@Attribute='VALUE']
//TAGNAME[@Attribute='VALUE' and @Attribute='value']
//*[@name='q']


"""
op.driver.get("https://www.google.in")
op.driver.find_element_by_xpath("//input[@name='q']").send_keys("Selenium python jobs in bangalore",Keys.ENTER)


time.sleep(2)
op.driver.quit()