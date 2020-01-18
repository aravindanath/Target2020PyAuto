from selenium.webdriver import Chrome
import time
path_win ="..//driver//chromedriver.exe"
path_mac ="..//driver//chromedriver"
driver= Chrome(executable_path=path_mac)

driver.get("https://www.google.com")
driver.fullscreen_window()

links =driver.find_elements_by_tag_name("a")
print("Total no of links:",len(links))

for ref in links:
    print(ref.text,"-->",ref.get_attribute("href"))


time.sleep(3)
driver.close()