from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\\webdrivers\chromedriver.exe")
driver.implicitly_wait(20)
driver.fullscreen_window()
win1=driver.window_handles[0]
driver.get("https://www.amazon.in/")
driver.switch_to.window(win1)
driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone xr yellow",Keys.ENTER)
time.sleep(4)
abc=driver.find_element_by_xpath("//span[contains(@class,'a-color-base a-text-normal')] [contains(text(),'Apple iPhone XR (64GB) - Yellow')]")
print(abc.text)
abc.click()
time.sleep(5)
win2=driver.window_handles[1]
driver.switch_to.window(win2)
print(win2)
driver.find_element_by_id("dp")
xyz=driver.find_element_by_xpath("//span[contains(@id,'priceblock_ourprice')]")
print("price of iphone in amazon", xyz.text)

driver.get("https://www.flipkart.com/")
try:
    driver.find_element_by_xpath("//button[text()='✕']").click()
    print("pop up handled")
except:
    print("no pop up")
driver.find_element_by_name("q").send_keys("iphone xr yellow",Keys.ENTER)

driver.find_element_by_xpath("//a[contains(@class,'_2cLu-l')] [contains(@title,'Apple iPhone XR (Yellow, 64 GB)')]").click()
window3=driver.window_handles[2]
time.sleep(5)
driver.switch_to.window(window3)
cost=driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']")
print("price of iphone in flipkart is",cost.text)
if xyz==cost:
    print("equal price in both")
else:
    print("mobile price is not equal")
time.sleep(4)
driver.quit()