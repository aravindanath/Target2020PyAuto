from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
import time

path = "../driver/chromedriver"

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(executable_path=path,options=ops)
driver.fullscreen_window()