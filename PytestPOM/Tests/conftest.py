import pytest
from selenium import webdriver
from Config.config import TestData

"""The file name of the conf should be 'conftest.py' always. Other browsers can be included in the 
fixtures params"""

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    
    """Test Setup"""
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.GECKO_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.maximize_window()
    
    yield
    
    """Test Teardown"""
    web_driver.quit()