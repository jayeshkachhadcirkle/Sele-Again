import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from openpyxl import worksheet
from pushbullet import Pushbullet
from plyer import notification

API_KEY = "o.QVhTjKwCECLRDhVEUPR8PJNhrIAgxipO"
pb = Pushbullet(API_KEY)

url = "https://www.justdial.com/Ahmedabad/Electrical-Shops/nct-10593097?trkid=340-ahmedabad&term=elec"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(5)

try:
    driver.find_element(By.XPATH, "//div[@aria-label='Best deal Modal Close Icon']").click()
    # continue
except:
    pass