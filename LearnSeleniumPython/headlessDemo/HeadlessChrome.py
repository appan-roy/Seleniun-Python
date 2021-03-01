from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from utility import DateUtils as du


opt = Options()
opt.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = opt)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)

print(driver.title)
assert "Orange" in driver.title

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

sleep(2)

driver.get_screenshot_as_file(os.getcwd()+"/Screenshots/"+"Selenium_"+du.get_current_timestamp()+".png")

driver.quit()