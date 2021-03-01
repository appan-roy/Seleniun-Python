from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# This will download the latest version of chromedriver and starts the test
driver = webdriver.Chrome(ChromeDriverManager().install())
 
driver.get("https://www.google.co.in/")
 
time.sleep(2)
 
driver.quit()


''' This will download the specific version of chromedriver and starts the test
driver = webdriver.Chrome(ChromeDriverManager("2.36").install())
 
driver.get("https://www.google.co.in/")
 
time.sleep(2)
 
driver.quit() '''