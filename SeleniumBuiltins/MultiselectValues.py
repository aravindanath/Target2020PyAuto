

from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

lp.driver.get("https://mdbootstrap.com/docs/jquery/forms/multiselect/")

lang = lp.driver.find_element_by_css_selector(".custom-select.browser-default")


sel = Select(lang)
sel.select_by_visible_text("One")
sel.select_by_visible_text("Two")
sel.select_by_visible_text("Three")
time.sleep(2)
sel.deselect_by_index(2)

sel.deselect_all()




time.sleep(5)
lp.driver.quit()



