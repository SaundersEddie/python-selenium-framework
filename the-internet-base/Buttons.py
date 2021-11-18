import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\webDrivers\\chromedriver_95.exe")
driver.maximize_window()

# Scenario: Ensure the functionality to add/remove button is correct
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text('Add/Remove Elements').click()
driver.find_element_by_xpath("//button[text()='Add Element']").click()
driver.find_element_by_xpath("//button[text()='Delete']").click()

# Scenario: Ensure the functionality to add/remove buttons is correct
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text('Add/Remove Elements').click()
for i in range(5):
    driver.find_element_by_xpath("//button[text()='Add Element']").click()
time.sleep(5)
for i in range(5):
    driver.find_element_by_xpath("//button[text()='Delete']").click()
time.sleep(5)

driver.close()
