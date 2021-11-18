import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\webDrivers\\chromedriver_95.exe")
driver.maximize_window()

# Scenario: Click checkboxes and validate clicked or unclicked status
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text('Checkboxes').click()

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for box in checkboxes:
    box.click()
time.sleep(5)


# Scenario: Select Option 1 then Option 2 on dropdown
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text('Dropdown').click()
dropdown = Select(driver.find_element_by_id('dropdown'))
dropdown.select_by_value('1')
time.sleep(5)
dropdown.select_by_value('2')
time.sleep(5)
driver.close()

