from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

# open the app
driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)

# assert home page text
homepage_text = driver.find_element(By.XPATH, "//*[@id='top']/div/h1").text
assert "CURA Healthcare Service" in homepage_text, "The CURA Healthcare Service is not present"

# click on make appointment button
if driver.find_element(By.ID, "btn-make-appointment").is_displayed():
    driver.find_element(By.ID, "btn-make-appointment").click()

# get username and password
username_text = driver.find_element("xpath", "//*[@id='login']/div/div/div[2]/form/div[1]/div[1]/div/div/input").get_attribute("value")
password_text = driver.find_element("xpath", "//*[@id='login']/div/div/div[2]/form/div[1]/div[2]/div/div/input").get_attribute("value")

# enter username
if driver.find_element("id", "txt-username").is_displayed():
    driver.find_element("id", "txt-username").clear()
    driver.find_element("id", "txt-username").send_keys(username_text)

# enter password
if driver.find_element_by_id("txt-password").is_displayed():
    driver.find_element_by_id("txt-password").clear()
    driver.find_element_by_id("txt-password").send_keys(password_text)

# click on login button
if driver.find_element_by_id("btn-login").is_displayed():
    driver.find_element_by_id("btn-login").click()

# select facility from dropdown
if driver.find_element("id", "combo_facility").is_displayed():
    Select(driver.find_element("id", "combo_facility")).select_by_visible_text("Seoul CURA Healthcare Center")

# select hospital readmission checkbox
if driver.find_element_by_name("hospital_readmission").is_displayed():
    if driver.find_element_by_name("hospital_readmission").is_selected() == False:
        driver.find_element_by_name("hospital_readmission").click()

# select health program radio button
if driver.find_element_by_name("programs").is_displayed():
    if driver.find_element_by_id("radio_program_medicare").is_selected():
        driver.find_element_by_id("radio_program_medicaid").click()

# select visit date
if driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[4]/div/div/div/span").is_displayed():
    driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/form/div[4]/div/div/div/span").click()
    
    dates = driver.find_elements(By.XPATH, "//div[@class='datepicker-days']/table//td")
    
    for date in dates:
        if date.text == "20":
            date.click()
            break

# enter comment
if driver.find_element("name", "comment").is_displayed():
    driver.find_element("name", "comment").clear()
    driver.find_element("name", "comment").send_keys("Appointment booked in Seoul")

# click on book appointment button
if driver.find_element(By.ID, "btn-book-appointment").is_displayed():
    driver.find_element(By.ID, "btn-book-appointment").click()

# assert appointment confirmation text
cnf_text = driver.find_element("xpath", "//*[@id='summary']/div/div/div[1]/h2").text
assert "Appointment Confirmation" in cnf_text, "Appointment Confirmation is not present"

# click on menu
if driver.find_element(By.XPATH, "//*[@id='menu-toggle']/i").is_displayed():
    driver.find_element(By.XPATH, "//*[@id='menu-toggle']/i").click()

# click on logout link text
if driver.find_element(By.LINK_TEXT, "Logout").is_displayed():
    driver.find_element(By.LINK_TEXT, "Logout").click()

# close the browser
sleep(2)
driver.quit()