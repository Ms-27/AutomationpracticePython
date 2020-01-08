from selenium import webdriver
import pytest

driver = webdriver.Opera(executable_path="/Users/Ms/Selenium webdriver driver/operadriver")

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Opera(executable_path="/Users/Ms/Selenium webdriver driver/operadriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    
def test_AP():    
    driver.get("http://automationpractice.com/index.php")

def teardown():
    driver.close()
    driver.quit()
    print("Test completed")