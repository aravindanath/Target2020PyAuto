# Test data

td={"url":"https://www.amazon.com","browser":"chrome"}

from  selenium.webdriver import Chrome,Firefox

pathChrome = "../driver/chromedriver"
pathFF ="../driver/geckodriver"
if td["browser"]=="chrome":
    driver= Chrome(pathChrome)
else:
    driver = Firefox(pathFF)


driver.get(td["url"])
driver.fullscreen_window()
driver.quit()

