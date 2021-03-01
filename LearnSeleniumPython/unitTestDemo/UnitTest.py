from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        
        super(GoogleSearch, cls).setUpClass()

        cls.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")

        cls.driver.maximize_window()

        cls.driver.implicitly_wait(10)
        
#     The test case name should start with test always.

    def test_search_Selenium(self):
        
        self.driver.get("https://www.google.co.in/")

        self.driver.find_element_by_name("q").send_keys("Selenium")

        self.driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
     
#     The test case name should start with test always.
       
    def test_search_Python(self):
        
        self.driver.get("https://www.google.co.in/")

        self.driver.find_element_by_name("q").send_keys("Python")

        self.driver.find_element_by_name("btnK1").send_keys(Keys.ENTER)
        
    @classmethod
    def tearDownClass(cls):
        
        super(GoogleSearch, cls).tearDownClass()
        
        cls.driver.quit()

        print("Test Completed")

# The below block is used to run the python unit test from IDE and terminal normally
# if __name__ == '__main__': 
#     unittest.main()

# The below block is used to run the python unit test from terminal with HTML reports
if __name__ == '__main__': 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:\Softwares\My PC Apps\Selenium Python\Workspace\LearnSeleniumPython\Reports'))
    
