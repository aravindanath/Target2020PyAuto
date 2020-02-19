from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

path='C:\\webdrivers\chromedriver.exe'
driver=Chrome(executable_path=path)
driver.fullscreen_window()
driver.get("https://www.hdfcbank.com/")

try:
    driver.find_element_by_xpath("//*[@id='popup_box']/a[2]/img").is_displayed()
    driver.find_element_by_xpath("//*[@id='popupBoxClose']").click()
    print("handled")
except BaseException:
    print("no popup")

driver.find_element_by_xpath("//*[@id='custom-button']/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div[12]/div[3]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/label/input").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='main']/div/div[12]/div[3]/div/div/div/div/div[2]/div[2]/div[2]/div[3]/a[1]").click()
time.sleep(5)
driver.quit()