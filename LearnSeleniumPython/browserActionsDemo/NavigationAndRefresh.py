from selenium import webdriver
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(20)

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

# navigate back
sleep(1)
driver.back()

# navigate forward
sleep(1)
driver.forward()

# page refresh
sleep(1)
driver.refresh()

sleep(1)
driver.quit()