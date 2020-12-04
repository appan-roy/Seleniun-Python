from selenium import webdriver
from time import sleep
import pytest

# Naming convention of the python file with PyTest is [test_*.py / *_test.py]
# Naming convention of the class is [Test*]
# Naming convention of the method is [test_*]

class TestSample():
    
    @pytest.fixture()
    def test_setup(self):
        
        global driver
    
        driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")

        driver.implicitly_wait(20)

        driver.maximize_window()
        
        yield   # This will work as test teardown
        
        driver.close()
    
        driver.quit()
        

    def test_login(self, test_setup):
        
        driver.get("https://opensource-demo.orangehrmlive.com/")

        driver.find_element_by_id("txtUsername").send_keys("Admin")
    
        driver.find_element_by_name("txtPassword").send_keys("admin123")
    
        driver.find_element_by_name("Submit").click()
    
        sleep(2)
