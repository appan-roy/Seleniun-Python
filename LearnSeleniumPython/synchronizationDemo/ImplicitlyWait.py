from selenium import webdriver


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

''' Implicitly wait : 
This is a dynamic wait/global wait. This is applicable for all the webelements once called. This is not 
applicable for non-webelements like title, alerts, url etc. The polling is 500 ms within the defined limit '''

driver.implicitly_wait(10)

uname_ele = driver.find_element("id", "txtUsername")
uname_ele.clear()
uname_ele.send_keys("Admin")

pwd_ele = driver.find_element("id", "txtPassword")
pwd_ele.clear()
pwd_ele.send_keys("admin123")

login_btn_ele = driver.find_element("id", "btnLogin")
login_btn_ele.click()

driver.quit()