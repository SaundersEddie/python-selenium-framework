from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\webDrivers\\chromedriver_95.exe")
driver.maximize_window()
driver.get("https://www.bbc.co.uk")
print(driver.title)

print(driver.current_url)
driver.close()


