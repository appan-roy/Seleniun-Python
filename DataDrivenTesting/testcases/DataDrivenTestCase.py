import lib.ExcelUtils
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("E:\Softwares\My PC Apps\Selenium Python\Webdrivers\chromedriver_win32/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

driver.maximize_window()

path = "E:\\Softwares\\My PC Apps\\Selenium Python\\Workspace\\DataDrivenTesting\\Test Data\\Data.xlsx"

rows = lib.ExcelUtils.getRowCount(path, "Cred")

for r in range(2, rows + 1):
    
    userid = lib.ExcelUtils.readData(path, "Cred", r, 1)  
    passkey = lib.ExcelUtils.readData(path, "Cred", r, 2)
    
    driver.find_element_by_id("txtUsername").clear()
    driver.find_element_by_id("txtUsername").send_keys(userid)
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys(passkey)
    driver.find_element_by_name("Submit").click()
    
    sleep(2)
    
    try:
        
        element=driver.find_element_by_link_text("Welcome Admin")
        
        lib.ExcelUtils.writeData(path, "Cred", r, 3, "Test passed")
        
    except NoSuchElementException:
        
        lib.ExcelUtils.writeData(path, "Cred", r, 3, "Test failed")
    

driver.quit()

print("Test completed")

