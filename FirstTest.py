from selenium import webdriver

driver = webdriver.Opera(executable_path="/Users/Ms/Selenium webdriver driver/operadriver")
driver.get("http://automationpractice.com/index.php")



driver.quit()

