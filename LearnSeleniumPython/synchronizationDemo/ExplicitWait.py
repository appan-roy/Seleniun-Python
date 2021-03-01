from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

''' Explicit wait : 
This is a dynamic wait. This is based on some expected conditions on both webelements and non-webelements 
like title, alerts, url etc. '''

wait = WebDriverWait(driver, 5)

# visibility of element located
uname_txtbx = wait.until(ec.visibility_of_element_located((By.NAME, "login")))
uname_txtbx.clear()
uname_txtbx.send_keys("Admin")

# element to be clickable
signin_btn = wait.until(ec.element_to_be_clickable((By.NAME, "proceed")))
signin_btn.click()

# alert to be present
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()

# presence of all elements located
footer_links = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='footer-area']/a")))
print(len(footer_links))
for link in footer_links:   print(link)

# element located to be selected
remember_chkbx = wait.until(ec.element_located_to_be_selected((By.NAME, "remember")))
print(remember_chkbx)

# presence of element located
new_acct_link = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Create a new account")))
new_acct_link.click()

driver.quit()