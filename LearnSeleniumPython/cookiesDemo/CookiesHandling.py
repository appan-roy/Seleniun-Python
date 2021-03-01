from selenium import webdriver
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(60)
driver.get("https://www.amazon.in/")
driver.implicitly_wait(20)

print(driver.get_cookies())

driver.add_cookie({'name':'selenium', 'domain':'amazon.in', 'value':'python'})

print(driver.get_cookies())

sleep(1)
driver.quit()