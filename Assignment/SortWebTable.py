from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("http://the-internet.herokuapp.com/tables")

dues = lp.driver.find_elements_by_xpath("//table[@id='table1']/tbody/tr/td[4]")

for d in dues:

    print(d.text)

lp.driver.find_element_by_xpath("//table[@id='table1']/thead/tr/th[4]").click()
time.sleep(2)
print("*"*100)
dues = lp.driver.find_elements_by_xpath("//table[@id='table1']/tbody/tr/td[4]")

empty=[]


for d in dues:
    empty.append(str(d.text).replace("$","").replace(".00",""))
    print(d.text)


empty.sort(reverse=True)
print(empty)


time.sleep(3)
lp.driver.close()