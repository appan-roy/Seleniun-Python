from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)

# Parent window
print("Parent window title : ", driver.title)
parent_window = driver.current_window_handle
print("Parent window : ", parent_window)

# Click on linkedIn
driver.find_element(By.XPATH, "//img[@alt='LinkedIn OrangeHRM group']").click()

# Child windows
child_windows = driver.window_handles

# Navigate to child window
for child in child_windows:
    print("Child window : ", child)
    if parent_window != child:
        driver.switch_to_window(child)
        print("Child window title : ", driver.title)
        driver.find_element(By.NAME, "email-or-phone").send_keys("Selenium")
        sleep(1)
        driver.close()

# switch back to parent window        
driver.switch_to_window(parent_window)
print("Parent window title : ", driver.title)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
sleep(1)
driver.quit()