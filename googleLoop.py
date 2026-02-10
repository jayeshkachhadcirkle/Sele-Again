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
from fake_useragent import UserAgent

queries = [
  "fashion store in bangkok",
  "fashion store in kuala lumpur",
  "fashion store in mumbai",
  "fashion store in delhi",
  "fashion store in bengaluru",
  "fashion store in chennai",
  "fashion store in hyderabad",
  "fashion store in dubai",
  "fashion store in abu dhabi",
  "fashion store in doha",
  "fashion store in riyadh",
  "fashion store in sydney",
  "fashion store in melbourne",
  "fashion store in brisbane",
  "fashion store in perth",
  "fashion store in cairo",
  "fashion store in johannesburg",
  "fashion store in cape town",
  "fashion store in nairobi",
  "fashion store in sao paulo",
  "fashion store in rio de janeiro",
  "fashion store in buenos aires",
  "fashion store in santiago",
  "fashion website in new york",
  "fashion website in los angeles",
  "fashion website in chicago",
  "fashion website in houston",
  "fashion website in san francisco",
  "fashion website in london",
  "fashion website in paris",
  "fashion website in berlin",
  "fashion website in madrid",
  "fashion website in rome",
  "fashion website in amsterdam",
  "fashion website in vienna",
  "fashion website in zurich",
  "fashion website in stockholm",
  "fashion website in toronto",
  "fashion website in vancouver",
  "fashion website in montreal",
  "fashion website in calgary",
  "fashion website in tokyo",
  "fashion website in osaka",
  "fashion website in seoul",
  "fashion website in beijing",
  "fashion website in shanghai",
  "fashion website in shenzhen",
  "fashion website in hong kong",
  "fashion website in singapore",
  "fashion website in bangkok",
  "fashion website in kuala lumpur",
  "fashion website in mumbai",
  "fashion website in delhi",
  "fashion website in bengaluru",
  "fashion website in chennai",
  "fashion website in hyderabad",
  "fashion website in dubai",
  "fashion website in abu dhabi",
  "fashion website in doha",
  "fashion website in riyadh",
  "fashion website in sydney",
  "fashion website in melbourne",
  "fashion website in brisbane",
  "fashion website in perth",
  "fashion website in cairo",
  "fashion website in johannesburg",
  "fashion website in cape town",
  "fashion website in nairobi",
  "fashion website in sao paulo",
  "fashion website in rio de janeiro",
  "fashion website in buenos aires",
  "fashion website in santiago",
  "apparel store in new york",
  "apparel store in los angeles",
  "apparel store in chicago",
  "apparel store in houston",
  "apparel store in san francisco",
  "apparel store in london",
  "apparel store in paris",
  "apparel store in berlin",
  "apparel store in madrid",
  "apparel store in rome",
  "apparel store in amsterdam",
  "apparel store in vienna",
  "apparel store in zurich",
  "apparel store in stockholm",
  "apparel store in toronto",
  "apparel store in vancouver",
  "apparel store in montreal",
  "apparel store in calgary",
  "apparel store in tokyo",
  "apparel store in osaka",
  "apparel store in seoul",
  "apparel store in beijing",
  "apparel store in shanghai",
  "apparel store in shenzhen",
  "apparel store in hong kong",
  "apparel store in singapore",
  "apparel store in bangkok",
  "apparel store in kuala lumpur",
  "apparel store in mumbai",
  "apparel store in delhi",
  "apparel store in bengaluru",
  "apparel store in chennai",
  "apparel store in hyderabad",
  "apparel store in dubai",
  "apparel store in abu dhabi",
  "apparel store in doha",
  "apparel store in riyadh",
  "apparel store in sydney",
  "apparel store in melbourne",
  "apparel store in brisbane",
  "apparel store in perth",
  "apparel store in cairo",
  "apparel store in johannesburg",
  "apparel store in cape town",
  "apparel store in nairobi",
  "apparel store in sao paulo",
  "apparel store in rio de janeiro",
  "apparel store in buenos aires",
  "apparel store in santiago",
  "apparel website in new york",
  "apparel website in los angeles",
  "apparel website in chicago",
  "apparel website in houston",
  "apparel website in san francisco",
  "apparel website in london",
  "apparel website in paris",
  "apparel website in berlin",
  "apparel website in madrid",
  "apparel website in rome",
  "apparel website in amsterdam",
  "apparel website in vienna",
  "apparel website in zurich",
  "apparel website in stockholm",
  "apparel website in toronto",
  "apparel website in vancouver",
  "apparel website in montreal",
  "apparel website in calgary",
  "apparel website in tokyo",
  "apparel website in osaka",
  "apparel website in seoul",
  "apparel website in beijing",
  "apparel website in shanghai",
  "apparel website in shenzhen",
  "apparel website in hong kong",
  "apparel website in singapore",
  "apparel website in bangkok",
  "apparel website in kuala lumpur",
  "apparel website in mumbai",
  "apparel website in delhi",
  "apparel website in bengaluru",
  "apparel website in chennai",
  "apparel website in hyderabad",
  "apparel website in dubai",
  "apparel website in abu dhabi",
  "apparel website in doha",
  "apparel website in riyadh",
  "apparel website in sydney",
  "apparel website in melbourne",
  "apparel website in brisbane",
  "apparel website in perth",
  "apparel website in cairo",
  "apparel website in johannesburg",
  "apparel website in cape town",
  "apparel website in nairobi",
  "apparel website in sao paulo",
  "apparel website in rio de janeiro",
  "apparel website in buenos aires",
  "apparel website in santiago",
  "formal wear store in new york",
  "formal wear store in los angeles",
  "formal wear store in chicago",
  "formal wear store in houston",
  "formal wear store in san francisco",
  "formal wear store in london",
  "formal wear store in paris",
  "formal wear store in berlin",
  "formal wear store in madrid",
  "formal wear store in rome",
  "formal wear store in amsterdam",
  "formal wear store in vienna",
  "formal wear store in zurich",
  "formal wear store in stockholm",
  "formal wear store in toronto",
  "formal wear store in vancouver",
  "formal wear store in montreal",
  "formal wear store in calgary",
  "formal wear store in tokyo",
  "formal wear store in osaka",
  "formal wear store in seoul",
  "formal wear store in beijing",
  "formal wear store in shanghai",
  "formal wear store in shenzhen",
  "formal wear store in hong kong",
  "formal wear store in singapore",
  "formal wear store in bangkok",
  "formal wear store in kuala lumpur",
  "formal wear store in mumbai",
  "formal wear store in delhi",
  "formal wear store in bengaluru",
  "formal wear store in chennai",
  "formal wear store in hyderabad",
  "formal wear store in dubai",
  "formal wear store in abu dhabi",
  "formal wear store in doha",
  "formal wear store in riyadh",
  "formal wear store in sydney",
  "formal wear store in melbourne",
  "formal wear store in brisbane",
  "formal wear store in perth",
  "formal wear store in cairo",
  "formal wear store in johannesburg",
  "formal wear store in cape town",
  "formal wear store in nairobi",
  "formal wear store in sao paulo",
  "formal wear store in rio de janeiro",
  "formal wear store in buenos aires",
  "formal wear store in santiago",
  "formal wear website in new york",
  "formal wear website in los angeles",
  "formal wear website in chicago",
  "formal wear website in houston",
  "formal wear website in san francisco",
  "formal wear website in london",
  "formal wear website in paris",
  "formal wear website in berlin",
  "formal wear website in madrid",
  "formal wear website in rome",
  "formal wear website in amsterdam",
  "formal wear website in vienna",
  "formal wear website in zurich",
  "formal wear website in stockholm",
  "formal wear website in toronto",
  "formal wear website in vancouver",
  "formal wear website in montreal",
  "formal wear website in calgary",
  "formal wear website in tokyo",
  "formal wear website in osaka",
  "formal wear website in seoul",
  "formal wear website in beijing",
  "formal wear website in shanghai",
  "formal wear website in shenzhen",
  "formal wear website in hong kong",
  "formal wear website in singapore",
  "formal wear website in bangkok",
  "formal wear website in kuala lumpur",
  "formal wear website in mumbai",
  "formal wear website in delhi",
  "formal wear website in bengaluru",
  "formal wear website in chennai",
  "formal wear website in hyderabad",
  "formal wear website in dubai",
  "formal wear website in abu dhabi",
  "formal wear website in doha",
  "formal wear website in riyadh",
  "formal wear website in sydney",
  "formal wear website in melbourne",
  "formal wear website in brisbane",
  "formal wear website in perth",
  "formal wear website in cairo",
  "formal wear website in johannesburg",
  "formal wear website in cape town",
  "formal wear website in nairobi",
  "formal wear website in sao paulo",
  "formal wear website in rio de janeiro",
  "formal wear website in buenos aires",
  "formal wear website in santiago",
  "sportswear store in new york",
  "sportswear store in los angeles",
  "sportswear store in chicago",
  "sportswear store in houston",
  "sportswear store in san francisco",
  "sportswear store in london",
  "sportswear store in paris",
  "sportswear store in berlin",
  "sportswear store in madrid",
  "sportswear store in rome",
  "sportswear store in amsterdam",
  "sportswear store in vienna",
  "sportswear store in zurich",
  "sportswear store in stockholm",
  "sportswear store in toronto",
  "sportswear store in vancouver",
  "sportswear store in montreal",
  "sportswear store in calgary",
  "sportswear store in tokyo",
  "sportswear store in osaka",
  "sportswear store in seoul",
  "sportswear store in beijing",
  "sportswear store in shanghai",
  "sportswear store in shenzhen",
  "sportswear store in hong kong",
  "sportswear store in singapore",
  "sportswear store in bangkok",
  "sportswear store in kuala lumpur",
  "sportswear store in mumbai",
  "sportswear store in delhi",
  "sportswear store in bengaluru",
  "sportswear store in chennai",
  "sportswear store in hyderabad",
  "sportswear store in dubai",
  "sportswear store in abu dhabi",
  "sportswear store in doha",
  "sportswear store in riyadh",
  "sportswear store in sydney",
  "sportswear store in melbourne",
  "sportswear store in brisbane",
  "sportswear store in perth",
  "sportswear store in cairo",
  "sportswear store in johannesburg",
  "sportswear store in cape town",
  "sportswear store in nairobi",
  "sportswear store in sao paulo",
  "sportswear store in rio de janeiro",
  "sportswear store in buenos aires",
  "sportswear store in santiago",
  "sportswear website in new york",
  "sportswear website in los angeles",
  "sportswear website in chicago",
  "sportswear website in houston",
  "sportswear website in san francisco",
  "sportswear website in london",
  "sportswear website in paris",
  "sportswear website in berlin",
  "sportswear website in madrid",
  "sportswear website in rome",
  "sportswear website in amsterdam",
  "sportswear website in vienna",
  "sportswear website in zurich",
  "sportswear website in stockholm",
  "sportswear website in toronto",
  "sportswear website in vancouver",
  "sportswear website in montreal",
  "sportswear website in calgary",
  "sportswear website in tokyo",
  "sportswear website in osaka",
  "sportswear website in seoul",
  "sportswear website in beijing",
  "sportswear website in shanghai",
  "sportswear website in shenzhen",
  "sportswear website in hong kong",
  "sportswear website in singapore",
  "sportswear website in bangkok",
  "sportswear website in kuala lumpur",
  "sportswear website in mumbai",
  "sportswear website in delhi",
  "sportswear website in bengaluru",
  "sportswear website in chennai",
  "sportswear website in hyderabad",
  "sportswear website in dubai",
  "sportswear website in abu dhabi",
  "sportswear website in doha",
  "sportswear website in riyadh",
  "sportswear website in sydney",
  "sportswear website in melbourne",
  "sportswear website in brisbane",
  "sportswear website in perth",
  "sportswear website in cairo",
  "sportswear website in johannesburg",
  "sportswear website in cape town",
  "sportswear website in nairobi",
  "sportswear website in sao paulo",
  "sportswear website in rio de janeiro",
  "sportswear website in buenos aires",
  "sportswear website in santiago",
  "luxury clothing store in new york",
  "luxury clothing store in los angeles",
  "luxury clothing store in chicago",
  "luxury clothing store in houston",
  "luxury clothing store in san francisco",
  "luxury clothing store in london",
  "luxury clothing store in paris",
  "luxury clothing store in berlin",
  "luxury clothing store in madrid",
  "luxury clothing store in rome",
  "luxury clothing store in amsterdam",
  "luxury clothing store in vienna",
  "luxury clothing store in zurich",
  "luxury clothing store in stockholm",
  "luxury clothing store in toronto",
  "luxury clothing store in vancouver",
  "luxury clothing store in montreal",
  "luxury clothing store in calgary",
  "luxury clothing store in tokyo",
  "luxury clothing store in osaka",
  "luxury clothing store in seoul",
  "luxury clothing store in beijing",
  "luxury clothing store in shanghai",
  "luxury clothing store in shenzhen",
  "luxury clothing store in hong kong",
  "luxury clothing store in singapore",
  "luxury clothing store in bangkok",
  "luxury clothing store in kuala lumpur",
  "luxury clothing store in mumbai",
  "luxury clothing store in delhi",
  "luxury clothing store in bengaluru",
  "luxury clothing store in chennai",
  "luxury clothing store in hyderabad",
  "luxury clothing store in dubai",
  "luxury clothing store in abu dhabi",
  "luxury clothing store in doha",
  "luxury clothing store in riyadh",
  "luxury clothing store in sydney",
  "luxury clothing store in melbourne",
  "luxury clothing store in brisbane",
  "luxury clothing store in perth",
  "luxury clothing store in cairo",
  "luxury clothing store in johannesburg",
  "luxury clothing store in cape town",
  "luxury clothing store in nairobi",
  "luxury clothing store in sao paulo",
  "luxury clothing store in rio de janeiro",
  "luxury clothing store in buenos aires",
  "luxury clothing store in santiago",
  "luxury clothing website in new york",
  "luxury clothing website in los angeles",
  "luxury clothing website in chicago",
  "luxury clothing website in houston",
  "luxury clothing website in san francisco",
  "luxury clothing website in london",
  "luxury clothing website in paris",
  "luxury clothing website in berlin",
  "luxury clothing website in madrid",
  "luxury clothing website in rome",
  "luxury clothing website in amsterdam",
  "luxury clothing website in vienna",
  "luxury clothing website in zurich",
  "luxury clothing website in stockholm",
  "luxury clothing website in toronto",
  "luxury clothing website in vancouver",
  "luxury clothing website in montreal",
  "luxury clothing website in calgary",
  "luxury clothing website in tokyo",
  "luxury clothing website in osaka",
  "luxury clothing website in seoul",
  "luxury clothing website in beijing",
  "luxury clothing website in shanghai",
  "luxury clothing website in shenzhen",
  "luxury clothing website in hong kong",
  "luxury clothing website in singapore",
  "luxury clothing website in bangkok",
  "luxury clothing website in kuala lumpur",
  "luxury clothing website in mumbai",
  "luxury clothing website in delhi",
  "luxury clothing website in bengaluru",
  "luxury clothing website in chennai",
  "luxury clothing website in hyderabad",
  "luxury clothing website in dubai",
  "luxury clothing website in abu dhabi",
  "luxury clothing website in doha",
  "luxury clothing website in riyadh",
  "luxury clothing website in sydney",
  "luxury clothing website in melbourne",
  "luxury clothing website in brisbane",
  "luxury clothing website in perth",
  "luxury clothing website in cairo",
  "luxury clothing website in johannesburg",
  "luxury clothing website in cape town",
  "luxury clothing website in nairobi",
  "luxury clothing website in sao paulo",
  "luxury clothing website in rio de janeiro",
  "luxury clothing website in buenos aires",
  "luxury clothing website in santiago"
]

# SEARCH_QUERY = "samsung mobiles in canada -site:amazon.com -site:samsung.com"
SEARCH_QUERY = "mens clothing store in toronto" + " \"add to cart\" \"products\""
OUTPUT_FILE = "search_results.json"
DELAY = 3  # seconds between page loads


def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    # reduce automation flags and set a random user agent when possible
    try:
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument(f"--user-agent={user_agent}")
    except Exception:
        # if fake_useragent is not available or fails, continue without it
        pass

    # experimental options to avoid automation flags
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Try to apply stealth protections if selenium_stealth is installed
    try:
        from selenium_stealth import stealth

        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
    except Exception:
        # If selenium_stealth isn't available or fails, continue anyway.
        # It's optional; the script will still run without it.
        pass

    # Make navigator.webdriver undefined in new pages (extra protection)
    try:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            },
        )
    except Exception:
        # Non-fatal if CDP command isn't supported
        try:
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        except Exception:
            pass

    return driver

def load_existing_results(filename):
    """Load existing results from JSON file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data) if isinstance(data, list) else set()
    except (FileNotFoundError, json.JSONDecodeError):
        return set()

def google_search_scraper(driver, query):
    """Run a Google search for `query` using the provided `driver` and
    return a list of found host URLs. The driver is NOT closed here so it
    can be reused across multiple queries.
    """
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
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        while True:
            time.sleep(DELAY)

            # Get search results links
            links = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf")

            divs = driver.find_elements(By.CLASS_NAME, "zReHs")
            for div in divs:
                try:
                    href = div.get_attribute("href")
                    parsed = urlparse(href)
                    host_only = f"{parsed.scheme}://{parsed.netloc}"
                    print("Link : ", href)
                    results.add(host_only)
                    save_to_json(list(results), OUTPUT_FILE)  # Save after each new link
                except Exception:
                    print("No href found")
                    continue

            # Try to go to next page
            try:
                next_button = driver.find_element(By.ID, "pnnext")
                next_button.click()
            except NoSuchElementException:
                print("Reached last page.")
                break

    except Exception as e:
        print("Error during scraping:", e)

    new_count = len(results) - initial_count
    print(f"Found {new_count} new URLs. Total: {len(results)}")
    return list(results)

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    driver = setup_driver()
    try:
        for q in queries:
            print(f"Processing query: {q}")
            SEARCH_QUERY = q + " \"add to cart\" \"products\""

            urls = google_search_scraper(driver, SEARCH_QUERY)
            save_to_json(urls, OUTPUT_FILE)
            print(f"Saved {len(urls)} URLs to {OUTPUT_FILE}")
            time.sleep(100)
    finally:
        driver.quit()


