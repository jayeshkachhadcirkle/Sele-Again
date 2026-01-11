import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

# wb = load_workbook('save_data.xlsx')
# ws = wb.active

driver = webdriver.Chrome()
driver.get("https://watchseries8.to/movie/the-tearsmith-watch-107806")
driver.maximize_window()

time.sleep(2)

x = driver.find_element(By.CSS_SELECTOR, "div[class='is-poster'] div[class='movie-thumbnail']")
print(x)

y = x.get_attribute("src")

print(y)
