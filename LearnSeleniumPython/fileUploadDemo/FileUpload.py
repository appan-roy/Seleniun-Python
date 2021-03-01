from selenium import webdriver
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")
driver.implicitly_wait(20)

driver.find_element("name", "upfile").send_keys("C:/Users/APPAN/Desktop/NSE Calc.xlsx")

driver.find_element("xpath", "//input[@type='submit']").click()

sleep(1)
driver.quit()