
from configparser import ConfigParser
from selenium. webdriver import Chrome
from selenium.webdriver.common.keys import Keys

config =  ConfigParser()
config.read("../testdata/data.ini")
url = config.get("Tc001","url")
search = config.get("Tc002","search")

driver = Chrome(executable_path="../driver/chromedriver")
driver.get(url)
driver.find_element_by_name('q').send_keys(search,Keys.ENTER)

# config.add_section("TC002")
# config.set("TC002","Password","passwoed#234")
#
# with open('Td.ini', 'w') as configfile:
#     config.write(configfile)