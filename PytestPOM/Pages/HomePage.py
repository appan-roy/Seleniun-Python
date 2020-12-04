from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    """Home Page Objects"""
    DASHBOARD_TAB = (By.XPATH, "//*[@id='menu_dashboard_index']/b")
    WELCOME_LINK = (By.ID, "welcome")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    
    """Page Actions for Home Page"""
    def get_home_page_title(self, title):
        return self.get_title(title)
    
    def is_dashboard_tab_visible(self):
        return self.is_visibled(self.DASHBOARD_TAB)
    
    def do_logout(self):
        self.do_click(self.WELCOME_LINK)
        self.do_click(self.LOGOUT_LINK)