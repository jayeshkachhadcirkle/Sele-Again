import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

# wb = load_workbook('save_data.xlsx')
# ws = wb.active

driver = webdriver.Chrome()
driver.get("https://coinmarketcap.com/")
driver.maximize_window()

# table = driver.find_element(By.CSS_SELECTOR, ".sc-ae0cff98-3.ipWPGi.cmc-table")
# table = driver.find_element(By.CSS_SELECTOR, ".sc-ae0cff98-3.ipWPGi.cmc-table").get_attribute('innerHTML')
table2 = driver.find_element(By.CSS_SELECTOR, ".sc-ae0cff98-3.ipWPGi.cmc-table").text

# print(table)
# print("=============")
# print(table2)

time.sleep(5)