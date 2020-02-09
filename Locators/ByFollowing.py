from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.toolsqa.com/automation-practice-table/")

xpath = "//div[@id='content']/table/tbody/tr/th[contains(text(),'TOWER')]//following::td[6]/a[text()='details']".replace("TOWER","Taipei 101")


tw =lp.driver.find_element_by_xpath(xpath)
print("Tower Details is present?",tw.is_displayed())
if tw.is_displayed():
    tw.click()


time.sleep(5)

lp.driver.quit()

# //button[text()='Sign Up' and starts-with(@id,'u_0')]//preceding::div[@class='_1lch']