from selenium import webdriver
from time import sleep
from testBrowsersDemo.ChromeTest import driver

# Naming convention of the python file with PyTest is test_*.py / *_test.py.
# The same thing applies to the naming convention of the functions as well.

def test_setup():
    
    global driver
    
    driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")

    driver.implicitly_wait(20)

    driver.maximize_window()

def test_login():
    
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.find_element_by_id("txtUsername").send_keys("Admin")

    driver.find_element_by_name("txtPassword").send_keys("admin123")

    driver.find_element_by_name("Submit").click()

    sleep(2)
    
    assert driver.title == "OrangeHRM"

def test_teardown():
    
    driver.close()

    driver.quit()
    
