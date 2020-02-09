from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys




op.driver.get("https://www.hdfcbank.com/")

"""

<button ng-if="mainctrl.userStatus == false " ng-click="mainctrl.login();
" type="button" class="btn btn-primary login-btn ng-scope" data-ol-has-click-handler="">Login</button>

//button[text()='Login']
(//button[text()='Login'])[2]
"""
time.sleep(2)
op.driver.find_element_by_xpath("(//button[text()='Login'])[2]").click()
time.sleep(2)
op.driver.find_element_by_xpath("//input[@type='radio' and @value=5]").click()
time.sleep(2)
op.driver.find_element_by_xpath("(//a[text()='Login'])[1]").click()
time.sleep(2)
op.driver.quit()