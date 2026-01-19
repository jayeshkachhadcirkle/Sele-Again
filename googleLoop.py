import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse

SEARCH_QUERY = "apparels site in dubai"
OUTPUT_FILE = "search_results.json"
DELAY = 2  # seconds between page loads

def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

def load_existing_results(filename):
    """Load existing results from JSON file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data) if isinstance(data, list) else set()
    except (FileNotFoundError, json.JSONDecodeError):
        return set()

def google_search_scraper(query):
    driver = setup_driver()
    results = load_existing_results(OUTPUT_FILE)
    initial_count = len(results)

    try:
        driver.get("https://www.google.com")
        time.sleep(DELAY)

        # Accept cookies if shown
        try:
            driver.find_element(By.XPATH, "//button[contains(., 'Accept')]").click()
            time.sleep(1)
        except NoSuchElementException:
            pass

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        while True:
            time.sleep(DELAY)

            # Get search results links
            links = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf")
            # print(links)
            # for link in links:
            #     print(link.get_attribute("href"))
            #     results.add(link.get_attribute("href"))

            divs = driver.find_elements(By.CLASS_NAME, "zReHs")
            # print(divs)
            for div in divs:
                try:
                    href = div.get_attribute("href")
                    parsed = urlparse(href)
                    host_only = f"{parsed.scheme}://{parsed.netloc}"
                    print("Link : ", href)
                    results.add(host_only)
                    save_to_json(list(results), OUTPUT_FILE)  # Save after each new link
                except:
                    print("No href found")
                    continue
            # Try to go to next page
            try:
                next_button = driver.find_element(By.ID, "pnnext")
                next_button.click()
            except NoSuchElementException:
                print("Reached last page.")
                break

    finally:
        driver.quit()

    new_count = len(results) - initial_count
    print(f"Found {new_count} new URLs. Total: {len(results)}")
    return list(results)

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    urls = google_search_scraper(SEARCH_QUERY)
    save_to_json(urls, OUTPUT_FILE)
    print(f"Saved {len(urls)} URLs to {OUTPUT_FILE}")
