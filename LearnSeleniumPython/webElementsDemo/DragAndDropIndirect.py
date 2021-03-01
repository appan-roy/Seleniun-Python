from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.implicitly_wait(20)

sleep(1)
src = driver.find_element(By.ID, "draggable")
tgt = driver.find_element(By.ID, "droppable")

act_chains = ActionChains(driver)

sleep(1)
act_chains.click_and_hold(src).move_to_element(tgt).release().perform()

sleep(1)
driver.quit()