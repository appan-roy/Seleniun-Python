from Config.config import TestData
from Tests.test_Base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

"""This is the test runner"""
class Test_Login_Logout(BaseTest):
    
    """Login Test"""
    def test_forgot_pwd_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_forgot_pwd_link_visible()
        assert flag
        
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

    """Logout Test"""
    def test_dashboard_tab_visible(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_dashboard_tab_visible()
        assert flag
        
    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        
    def test_logout(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_logout()