import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

element = driver.find_element_by_id("APjFqb")

element.click()
time.sleep(3)
