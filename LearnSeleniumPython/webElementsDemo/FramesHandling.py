from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.redbus.in/")
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//i[contains(@id, 'profile')]").click()
driver.find_element(By.ID, "signInLink").click()

sleep(2)

driver.switch_to_frame(driver.find_element(By.XPATH, "//iframe[@class='modalIframe']"))
driver.switch_to_frame(driver.find_element(By.XPATH, "//iframe[@title='Sign in with Google Button']"))

driver.find_element(By.XPATH, "//span[text()='Sign in with Google']").click()

sleep(2)

driver.quit()