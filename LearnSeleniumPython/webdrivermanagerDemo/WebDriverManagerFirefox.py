from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time


# This will download the latest version of geckodriver and starts the test
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
 
driver.get("https://www.google.co.in/")
 
time.sleep(2)
 
driver.quit()