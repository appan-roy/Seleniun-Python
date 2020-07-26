class Homepage():

# This __init__(self) constructor will be called every time when an object for this class is created. 
    def __init__(self, driver):
        
        self.driver = driver
        
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
        
    def click_welcome(self):
        
        self.driver.find_element_by_id(self.welcome_link_id).click()
        
    def click_logout(self):
        
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
        
    