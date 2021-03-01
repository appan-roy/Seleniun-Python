class homePage():

    # capture home page objects
    welcome_id = "welcome"
    logout_xpath = "//*[@id='welcome-menu']/ul/li[2]/a"
    
    # create constructor
    def __init__(self, driver):
        self.driver = driver
        
    # create methods       
    def clickOnWelcome(self):
        self.driver.find_element_by_id(self.welcome_id).click()
        
    def clickOnLogoutLink(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()