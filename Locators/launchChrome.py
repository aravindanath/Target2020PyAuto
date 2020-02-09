
from selenium.webdriver import ChromeOptions,Chrome
path ="../driver/chromedriver"

ops= ChromeOptions()
ops.add_argument("--disable-notifications")
# ops.add_argument("--headless")
driver = Chrome(executable_path=path,options=ops)
