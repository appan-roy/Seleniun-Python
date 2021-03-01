import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):

    def test_assertEqual(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        self.assertEqual("Google", self.driver.title, "The page titles are not same")
        self.driver.close()

    def test_assertNotEqual(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        self.assertNotEqual("Google", self.driver.title, "The page titles are same")
        self.driver.close()
        
    def test_assertTrue(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        page_title = self.driver.title
        self.assertTrue(page_title == 'Google', "The page titles are not same")
        self.driver.close()
        
    def test_assertFalse(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        page_title = self.driver.title
        self.assertFalse(page_title == 'Google', "The page titles are same")
        self.driver.close()
        
    def test_assertIsNone(self):
        self.driver = None
        self.assertIsNone(self.driver, "The driver is not none")
        
    def test_assertIsNotNone(self):
        self.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
        self.assertIsNotNone(self.driver, "The driver is none")
        self.driver.close()
        
    def test_assertIn(self):
        myList = ['python', 'java', 'javascript']
        self.assertIn('python', myList, 'item is not found in the list')
        
    def test_assertNotIn(self):
        myList = ['python', 'java', 'javascript']
        self.assertNotIn('ruby', myList, 'item is found in the list')
        
    def test_assertGreater(self):
        self.assertGreater(7, 3, 'first number is not greater than the second number')
        
    def test_assertGreaterEqual(self):
        self.assertGreaterEqual(7, 7, 'first number is not greater than or equal to the second number')
        
    def test_assertLess(self):
        self.assertLess(3, 7, 'first number is not less than the second number')
        
    def test_assertLessEqual(self):
        self.assertLessEqual(7, 7, 'first number is not less than or equal to the second number')

# the below block is used to run as python-run
if __name__ == "__main__":
    unittest.main()