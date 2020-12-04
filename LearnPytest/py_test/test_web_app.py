from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com")
    assert driver.title == "Gmail"
    driver.quit()
    
def test_linkedIn():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://in.linkedin.com/")
    assert driver.title == "LinkedIn India: Log In or Sign Up"
    driver.quit()
    
def test_instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()