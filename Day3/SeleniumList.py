from selenium.webdriver import Chrome
import time
path_win ="..//driver//chromedriver.exe"
path_mac ="..//driver//chromedriver"
driver= Chrome(executable_path=path_mac)
driver.get("https://www.wikipedia.org/")
driver.fullscreen_window()
driver.find_element_by_xpath("//*[@id=\"search-input\"]/div[1]/div").click()
time.sleep(5)
lang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")
print("Total no of lang",len(lang))
empty=[]
for ref in lang:
    empty.append(ref.text)
    if ref.text == "Français":
        ref.click()


print("Before sort",empty)
empty.sort()
print("After sort",empty)
time.sleep(5)
driver.close()
