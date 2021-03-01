import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    
    # the test case name should start with test always
    def test_Google(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("The title of the page is : ", self.driver.title)
        self.driver.close()
    
    # the test case name should start with test always
    def test_Bing(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("The title of the page is : ", self.driver.title)
        self.driver.close()

# the below block is used to run as python-run
if __name__ == "__main__":
    unittest.main()