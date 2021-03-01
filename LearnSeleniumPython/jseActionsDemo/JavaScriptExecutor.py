from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("https://www.amazon.in/")
driver.implicitly_wait(20)

# type into textbox
sleep(1)
searchbox = driver.find_element(By.ID, "twotabsearchtextbox")
driver.execute_script("arguments[0].value='iphone'", searchbox)

# scroll to the bottom of the page
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# scroll to the top of the page
sleep(1)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

# scroll into view
sleep(1)
about_us_link = driver.find_element(By.LINK_TEXT, "About Us")
driver.execute_script("arguments[0].scrollIntoView(true);", about_us_link)

# scroll to the top of the page
sleep(1)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

# solid red border around best sellers link
sleep(1)
best_sellers_link = driver.find_element(By.LINK_TEXT, "Best Sellers")
driver.execute_script("arguments[0].style.border = '3px solid red';", best_sellers_link)

# click on best sellers link
sleep(1)
driver.execute_script("arguments[0].click;", best_sellers_link)

# get page title
sleep(1)
title = driver.execute_script("return document.title;")
print(title)

# generate alert
sleep(1)
driver.execute_script("alert('hello selenium');")
driver.switch_to_alert().accept()

sleep(1)
driver.quit()