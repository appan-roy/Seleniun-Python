class loginPage():
    
    # capture login page objects
    uname_id = "txtUsername"
    pwd_id = "txtPassword"
    login_button_id = "btnLogin"
    
    # create constructor
    def __init__(self, driver):
        self.driver = driver
        
    # create methods
    def enterUsername(self, username):
        self.driver.find_element_by_id(self.uname_id).send_keys(username)
        
    def enterPassword(self, password):
        self.driver.find_element_by_id(self.pwd_id).send_keys(password)
        
    def clickOnLoginBtn(self):
        self.driver.find_element_by_id(self.login_button_id).click()