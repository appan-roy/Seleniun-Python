from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)

# Alert with OK
driver.find_element(By.XPATH, ".//button[@class='btn btn-danger']").click()
alert = driver.switch_to_alert()
sleep(1)
print(alert.text)
alert.accept()

# Alert with OK and Cancel
driver.find_element(By.XPATH, ".//div[@class='container center']//li/a[contains(text(), 'Alert with OK & Cancel ')]").click()
driver.find_element(By.XPATH, ".//button[@class='btn btn-primary']").click()
alert = driver.switch_to_alert()
sleep(1)
print(alert.text)
alert.accept()
driver.find_element(By.XPATH, ".//button[@class='btn btn-primary']").click()
alert = driver.switch_to_alert()
sleep(1)
print(alert.text)
alert.dismiss()

# Alert with Textbox
driver.find_element(By.XPATH, ".//div[@class='container center']//li/a[contains(text(), 'Alert with Textbox ')]").click()
driver.find_element(By.XPATH, ".//button[@class='btn btn-info']").click()
alert = driver.switch_to_alert()
sleep(1)
print(alert.text)
alert.accept()
driver.find_element(By.XPATH, ".//button[@class='btn btn-info']").click()
alert = driver.switch_to_alert()
sleep(1)
print(alert.text)
alert.dismiss()

driver.quit()