from browserLaunch import launchChrome as lp
import time

lp.driver.get("http://the-internet.herokuapp.com/upload")


lp.driver.find_element_by_css_selector("#file-upload").send_keys("/Users/aravindanathdm/PycharmProjects/Target2020PyAuto/SeleniumBuiltins/Agenda.txt")
time.sleep(3)
lp.driver.find_element_by_css_selector("#file-submit").click()
time.sleep(3)



lp.driver.get("http://the-internet.herokuapp.com/download")


lp.driver.find_element_by_link_text("Agenda.txt").click()

time.sleep(3)
lp.driver.quit()