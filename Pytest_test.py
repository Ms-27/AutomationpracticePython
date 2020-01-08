from selenium import webdriver
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Opera(executable_path="/Users/Ms/Selenium webdriver driver/operadriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test completed")
    
def test_AP():    
    driver.get("http://automationpractice.com/index.php")
