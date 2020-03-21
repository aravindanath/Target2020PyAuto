from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys


lp.driver.get("https://www.espncricinfo.com/series/19237/scorecard/1183533/australia-vs-new-zealand-2nd-test-new-zealand-in-australia-2019-20")

# //*[@name='q']--> * ALL the elements
lp.driver.find_element_by_xpath("(//a[contains(text(),'DA ')])[1]").click()

# (//input[contains(@value,'Search')])[2]
# //input[contains(@class,'inputtext login_form_input_box') and @id='email']

time.sleep(3)
# //span[contains(text(),'Hello, Sign in') or contains(text(),'Hello. Sign in') ]

lp.driver.get("https://www.amazon.com")
lp.driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in') or contains(text(),'Hello. Sign in') ]").click()
print(lp.driver.current_url)

time.sleep(3)

lp.driver.get("https://www.amazon.in")
lp.driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in') or contains(text(),'Hello. Sign in') ]").click()
print(lp.driver.current_url)
time.sleep(3)
lp.driver.quit()

