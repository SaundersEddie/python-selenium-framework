import time
from selenium import webdriver
# from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\webDrivers\\chromedriver_95.exe")
driver.maximize_window()

# Scenario: When I enter a web page I close a modal popup
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text('Entry Ad').click()
time.sleep(5)
driver.find_element_by_css_selector(".modal-footer > p").click()
time.sleep(5)

# Scenario: When I exit a web page I close a modal popup
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text('Exit Intent').click()
time.sleep(5)


driver.close()