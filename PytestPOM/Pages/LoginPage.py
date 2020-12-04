from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class LoginPage(BasePage):
    
    """Login Page Objects"""
    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    FORGOT_PWD_LINK = (By.LINK_TEXT, "Forgot your password?")
    
    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    """Page Actions for Login Page"""
    def get_login_page_title(self, title):
        return self.get_title(title)
    
    def is_forgot_pwd_link_visible(self):
        return self.is_visibled(self.FORGOT_PWD_LINK)
    
    def do_login(self, uname, pwd):
        self.do_send_keys(self.USERNAME, uname)
        self.do_send_keys(self.PASSWORD, pwd)
        self.do_click(self.LOGIN_BUTTON)