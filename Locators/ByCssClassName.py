
from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.icicibank.com/#")
# . is used for identify class attribute
# //span[@class='value']
# "value"
lp.driver.find_element_by_css_selector(".pl-login-ornage-box").click()
time.sleep(5)

lp.driver.quit()

