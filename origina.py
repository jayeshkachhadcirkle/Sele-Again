import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:/Users/jayes/AppData/Local/Google/Chrome/User Data") #Path to your chrome profile
# driver = webdriver.Chrome(executable_path="C:/Users/chromedriver.exe", chrome_options=options)
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(options=options)

driver.get("www.google.in")
time.sleep(5)