from browserLaunch import launchChrome as lp
import time
lp.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

lp.driver.find_element_by_css_selector("input[type='submit']").click()
time.sleep(2)
alert = lp.driver.switch_to.alert
alert.accept()
lp.driver.find_element_by_css_selector("#login1").send_keys("arvind")


time.sleep(2)

lp.driver.get("http://the-internet.herokuapp.com/javascript_alerts")

lp.driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()

alert = lp.driver.switch_to.alert
print(alert.text)
alert.accept()


txt =lp.driver.find_element_by_css_selector("#result").text

print(txt)

lp.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()

alert = lp.driver.switch_to.alert
print(alert.text)
alert.dismiss()

txt =lp.driver.find_element_by_css_selector("#result").text

print(txt)

lp.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()

alert = lp.driver.switch_to.alert
print(alert.text)
alert.send_keys("Hi all")
alert.accept()

txt =lp.driver.find_element_by_css_selector("#result").text

print(txt)






def acceptAlert():
    alert =lp.driver.switch_to.alert
    print(alert.text)
    alert.accept()


def dismissAlert():
    alert =lp.driver.switch_to.alert
    print(alert.text)
    alert.dismiss()

def sendKeys(value):
    alert =lp.driver.switch_to.alert
    print(alert.text)
    alert.send_keys(value)
