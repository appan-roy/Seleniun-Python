from selenium import webdriver
import pytest
import allure
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class TestOrangeHRM():
    
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        
        logo_status = self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        
        if logo_status == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), 
                          name = "testlogo",
                          attachment_type = AttachmentType.PNG)
            assert False
        
        self.driver.close()
    
    @allure.severity(allure.severity_level.NORMAL)    
    def test_listEmployees(self):
        pytest.skip("This test case is not ready yet", allow_module_level=False)
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        
        page_title = self.driver.title
        
        if page_title == "OrangeHRM123":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), 
                          name = "testlogin",
                          attachment_type = AttachmentType.PNG)
            assert False
        
        self.driver.close()