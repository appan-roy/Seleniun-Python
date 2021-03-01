from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(20)

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

sleep(3)
act_chains = ActionChains(driver)

sleep(1)
admin_ele = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
act_chains.move_to_element(admin_ele).perform()

sleep(1)
user_mgmt_ele = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
act_chains.move_to_element(user_mgmt_ele).perform()

sleep(1)
users_ele = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")
users_ele.click()

sleep(1)
driver.quit()