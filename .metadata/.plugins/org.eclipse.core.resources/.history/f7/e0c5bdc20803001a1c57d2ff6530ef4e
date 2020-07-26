from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.set_page_load_timeout(30)

driver.maximize_window()

driver.implicitly_wait(20)

driver.get_screenshot_as_file("E:\\Softwares\\My PC Apps\\Selenium Python\\Workspace\\LearnSeleniumPython\\Screenshots\\BeforeLoginChrome.png")

print(driver.title)

assert "Orange" in driver.title

driver.find_element_by_id("txtUsername").send_keys("Admin")

driver.find_element_by_name("txtPassword").send_keys("admin123")

driver.find_element_by_id("btnLogin").click()

sleep(2)

driver.get_screenshot_as_file("E:\\Softwares\\My PC Apps\\Selenium Python\\Workspace\\LearnSeleniumPython\\Screenshots\\AfterLoginChrome.png")

driver.quit()