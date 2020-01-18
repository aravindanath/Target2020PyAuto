from selenium import webdriver
path = "../driver/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://www.wikipedia.org/")
driver.fullscreen_window()

links = driver.find_elements_by_tag_name("a")
empty =[]
print("Total no of links",len(links))
for link in links:
    print(link.text," ----> ",link.get_attribute('href'))




print("Empty list",empty)
driver.quit()