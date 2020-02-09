
"""

https://chromedriver.chromium.org/capabilities
https://selenium.dev/selenium/docs/api/java/org/openqa/selenium/chrome/ChromeOptions.html
https://selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/chrome_exports_Options.html

"""

from selenium.webdriver import ChromeOptions,Chrome
path ="../driver/chromedriver"
# in win u must give chromedriver.exe
# webdriver.Firefox(executable_path=path)
ops = ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_argument("--headless")
driver = Chrome(executable_path=path,options=ops)
baseUrl ="https://www.facebook.com/"
driver.get(baseUrl)
print("Home page title ",driver.title)


driver.close()