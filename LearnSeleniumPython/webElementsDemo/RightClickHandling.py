from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(20)

act_chains = ActionChains(driver)

right_click_ele = driver.find_element(By.XPATH, "//span[text()='right click me']")
act_chains.context_click(right_click_ele).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR, "li.context-menu-icon span")

sleep(1)
for opt in right_click_options:
    if opt.text == 'Edit':
        opt.click()
        driver.switch_to_alert().accept()
        
sleep(1)
driver.quit()