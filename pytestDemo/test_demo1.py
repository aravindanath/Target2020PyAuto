from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_logina():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    print("login test")


def test_loginb():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.com")
    print("login test")
    print(driver.title)