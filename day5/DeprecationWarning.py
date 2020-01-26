import LaunchBrowsers.openBrowser as op

op.driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
print(op.driver.title)

# old
op.driver.switch_to_frame("packageListFrame")
# latest
op.driver.switch_to.frame("packageListFrame")

"""
DeprecationWarning: use driver.switch_to.frame instead
  op.driver.switch_to_frame("packageListFrame")
"""

# op.driver.find_element_by_link_text("Appium").click()

"""
selenium.common.exceptions.NoSuchElementException:
Message: no such element: Unable to locate element: {"method":"link text","selector":"Appium"}
"""
# op.driver.switch_to.frame("")
print(op.driver.title)
op.driver.close()