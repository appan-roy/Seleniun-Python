from selenium import webdriver
import unittest
import HtmlTestRunner
from pages.LoginPage import loginPage
from pages.HomePage import homePage


class loginTest(unittest.TestCase):
    
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    driver = webdriver.Chrome("../drivers/chromedriver.exe")
    
    @classmethod
    def setUpClass(cls):
        
        super(loginTest, cls).setUpClass()

        cls.driver.maximize_window()
        
        cls.driver.get(cls.baseUrl)
        
    # The test case name should start with test always.
    def test_orangeHrm_Login(self):
        
        lp = loginPage(self.driver)
        
        lp.enterUsername(self.username)
        
        lp.enterPassword(self.password)
        
        lp.clickOnLoginBtn()
        
        self.assertEqual("OrangeHRM", self.driver.title, "Page title are not same")
        
    # The test case name should start with test always.
    def test_orangeHrm_Logout(self):
        
        hp = homePage(self.driver)
        
        hp.clickOnWelcome()
        
        hp.clickOnLogoutLink()
        
    @classmethod
    def tearDownClass(cls):
        
        super(loginTest, cls).tearDownClass()
        
        cls.driver.quit()

        print("Test Completed")

# The below block is used to run the python unit test from terminal with HTML reports
if __name__ == '__main__': 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports/'))
    