
from selenium.webdriver import ChromeOptions,Chrome
path ="../driver/chromedriver"
# in win u must give chromedriver.exe
# webdriver.Firefox(executable_path=path)
ops = ChromeOptions()
ops.add_argument("--disable-notifications")

driver = Chrome(executable_path=path,options=ops)
baseUrl ="https://www.icicibank.com/"
driver.get(baseUrl)
print("Home page title ",driver.title)
driver.find_element_by_class_name("pl-login-ornage-box").click()
print("Login page title ",driver.title)

driver.close()