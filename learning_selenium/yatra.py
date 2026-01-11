import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://secure.yatra.com/")
driver.maximize_window()

time.sleep(1)

# login-input
#
# loginClick = driver.find_element(By.ID, 'login-input').send_keys('7818922430')
# time.sleep(1)

# driver.find_element(By.ID, 'login-continue-btn').click()

list_a = driver.find_elements(By.TAG_NAME, 'a')

print(len(list_a))

for a in list_a:
    print(a.text)

# time.sleep()
