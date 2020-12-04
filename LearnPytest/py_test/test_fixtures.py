from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("-------------------set up------------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    
    yield   # this keyword will work as tear down
    print("-------------------tear down------------------------")
    driver.quit()

def test_google_title(init_driver):
    assert driver.title == "Google"

def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.com/"