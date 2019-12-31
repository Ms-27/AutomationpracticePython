from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Opera(executable_path="/Users/Ms/Selenium webdriver driver/operadriver")
driver.get("http://automationpractice.com/index.php")

ErrMsg = 'Problem'

assert driver.current_url == 'http://automationpractice.com/index.php', ErrMsg
assert driver.title == 'My Store', ErrMsg

driver.refresh()
#driver.get_screenshot_as_file('./screenshots/scr01.png')

bestsellers_btn = driver.find_element_by_xpath("//a[contains(@class, 'blockbestsellers')]")

assert bestsellers_btn.is_displayed()

wait = WebDriverWait(driver, 10)


driver.quit()

