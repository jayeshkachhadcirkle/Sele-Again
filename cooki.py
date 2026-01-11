import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
import pickle

url = "https://www.linkedin.com/feed/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(30)

pickle.dump(driver.get_cookies(), open("cookies_linkedin.pkl", "wb"))
time.sleep(5)

print("finished")


