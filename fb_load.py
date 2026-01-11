import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

url = "https://www.facebook.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(3)

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.get(url)
time.sleep(2)

driver.get("https://www.facebook.com/search/people?q=himmatnagar")

element = driver.find_element(By.XPATH, "//div[@class='x6s0dn4 x78zum5 xdt5ytf x193iq5w x1t2pt76 xh8yej3']")

scrollorigin = ScrollOrigin.from_element(element)
print(scrollorigin)
scrolltarget = 3000

e1 = 0

while True:
    try:
        driver.find_element(By.XPATH, "//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w x1gslohp x12nagc xzboxd6 x14l7nz5']")
        print("E0.1")
        ActionChains(driver).scroll_from_origin(scrollorigin, 0, 100).perform()
        break
    except:
        try:
            ActionChains(driver).scroll_from_origin(scrollorigin, 0, scrolltarget).perform()
            # scrollorigin = scrollorigin + 3000
            scrolltarget = scrolltarget + 4000
            print(scrolltarget)
            time.sleep(2)
            e1 = 0
        except:
            time.sleep(2)
            print("E1")
            e1 = e1 + 1
            if e1 > 10:
                break
            else:
                pass
            continue

time.sleep(2)

hover_ele = driver.find_elements(By.XPATH, "(//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1sur9pj xkrqix3 xzsf02u x1s688f'])")

for i in range(len(hover_ele)):
    hover = ActionChains(driver).move_to_element(hover_ele[i]).perform()
    # time.sleep(3)
    try:
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'][normalize-space()='Message'])[1]")))
        driver.find_element(By.XPATH, "(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'][normalize-space()='Message'])[1]").click()
    except:
        sidehover = ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "a[aria-label='Home']")).perform()
        continue
    time.sleep(1)

    wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
    wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='xat24cr xdj266r']")))

    try:
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='html-div xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a xyk4ms5'])[1](//div[@class='html-div xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a xyk4ms5'])[1]")))
        print("already sent")
        continue
    except:
        pass

    try:
        driver.find_element(By.XPATH, "//p[@class='xat24cr xdj266r']").send_keys("Want to know best tax saving investment option? \n https://api.whatsapp.com/send/?phone=917990439256&text=Want+to+know+more+about+this+plan ")
        driver.find_element(By.CSS_SELECTOR, "div[aria-label='Press enter to send']").click()
    except:
        sidehover = ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "a[aria-label='Home']")).perform()
        print("Unabel to send")
        continue
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div[aria-label='Close chat'] svg").click()
    time.sleep(0.5)

print("Fini")