from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.action_chains import ActionChains
lp.driver.get("https://www.myntra.com/")

women =lp.driver.find_element_by_xpath("(//a[text()='Women'])[1]")
flats = lp.driver.find_element_by_xpath("(//a[text()='Flats'])[1]")

act =ActionChains(lp.driver)
act.move_to_element(women).perform()

act.click(flats).perform()


listOfflats = lp.driver.find_element_by_xpath("//ul[@class='results-base']/li[10]")


listOfflats.click()
time.sleep(3)
lp.driver.close()

time.sleep(3)
lp.driver.quit()


