from selenium import webdriver
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.implicitly_wait(20)

sleep(1)
driver.quit()