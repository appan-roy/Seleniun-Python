from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl.workbook.workbook import Workbook

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, ".//input[contains(@id,'search')]").send_keys("iphone")
driver.find_element(By.XPATH, ".//input[contains(@value,'Go')]").click()

sleep(3)

phones = driver.find_elements(By.XPATH, ".//span[contains(@class,'a-color-base a-text-normal')]")
prices = driver.find_elements(By.XPATH, ".//span[contains(@class,'a-price-whole')]")

phone_names = []
phone_prices = []

for phone in phones:
    phone_names.append(phone.text)
    
for price in prices:
    phone_prices.append(price.text)
    
final_list = zip(phone_names, phone_prices)

wb = Workbook()
wb['Sheet'].title = 'iPhone Data'
sheet = wb.active

sheet.append(["Phone Name", "Price"])

for i in list(final_list):
    sheet.append(i)

wb.save("iPhonesList.xlsx")

driver.quit()