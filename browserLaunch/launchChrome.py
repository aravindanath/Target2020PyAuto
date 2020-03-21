
from selenium.webdriver import Chrome,ChromeOptions

path = "../driver/chromedriver"

ops = ChromeOptions()
ops.add_argument('--ignore-certificate-errors')
ops.add_argument("--disable-notifications")
driver = Chrome(executable_path=path,options=ops)
driver.fullscreen_window()
# driver.implicitly_wait(10)
# driver.set_script_timeout(100)