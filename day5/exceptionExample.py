from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="../driver/chromedriver")

driver.get("https://www.hdfcbank.com/")

try:
    driver.find_element_by_xpath("//a[text()='X']").click()
    time.sleep(3)
    driver.find_element_by_xpath("(//button[text()='Login'])[2]").click()
    time.sleep(2)
    print(driver.title)
except :
    print("Popup did not appear")

finally:
    print("closing browser....")
    driver.quit()

