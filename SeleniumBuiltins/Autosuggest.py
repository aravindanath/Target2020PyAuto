

from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
lp.driver.get("https://www.redbus.in/")

lp.driver.find_element_by_css_selector("#src").send_keys("Hyd")
time.sleep(2)
srclist = lp.driver.find_elements_by_xpath("//ul[@class='autoFill']/li")

print("No of pickup points",len(srclist))

for li in srclist:
    # print(li.text)
    if li.text == "Bhel, Hyderabad":
        li.click()
        break


lp.driver.find_element_by_css_selector("#dest").send_keys("Bangalore (All Locations)",Keys.ENTER)

lp.driver.find_element_by_css_selector(".icon-onward-calendar.icon").click()

onWardCal =  lp.driver.find_elements_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td")

for li in onWardCal:
    if li.text == "10":
        li.click()
        break


lp.driver.find_element_by_css_selector(".icon-return-calendar.icon").click()

returnDate = lp.driver.find_elements_by_xpath("//div[@id='rb-calendar_return_cal']/table/tbody/tr/td")


for li in returnDate:
    if li.text != "Apr 2020":
        lp.driver.find_element_by_xpath("(//button[text()='>'])[2]").click()
        break



returnDate = lp.driver.find_elements_by_xpath("//div[@id='rb-calendar_return_cal']/table/tbody/tr/td")


for li in returnDate:
    if li.text == "20":
        li.click()
        break

lp.driver.find_element_by_css_selector("#search_btn").click()




time.sleep(5)
# lp.driver.quit()



