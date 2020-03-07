

from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

lp.driver.get("https://www.wikipedia.org/")

lang = lp.driver.find_element_by_xpath("//select[@id='searchLanguage']")


sel = Select(lang)
sel.select_by_visible_text("Galego")
time.sleep(5)
sel.select_by_index(0)
time.sleep(5)
sel.select_by_value("mk")

time.sleep(5)
lp.driver.quit()



