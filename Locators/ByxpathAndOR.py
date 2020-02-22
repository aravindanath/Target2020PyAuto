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
lp.driver.get("https://www.facebook.com")
lp.driver.find_element_by_xpath("//input[@type='text' and @name='firstname' or @id='u_0_m']").send_keys("Arvind",Keys.ENTER)


time.sleep(2)
lp.driver.quit()