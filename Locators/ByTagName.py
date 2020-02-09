from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys


lp.driver.get("https://www.google.com")

links = lp.driver.find_elements_by_tag_name("a")

print("Total no of links: ",len(links))

for ln in links:
    print(ln.text,"-->",ln.get_attribute("href"))


time.sleep(3)
lp.driver.quit()
