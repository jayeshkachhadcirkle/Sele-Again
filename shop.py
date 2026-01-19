import json
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin, urlparse

class ShopifyContactScraper:
    def __init__(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in background
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.results = []
    
    def get_sitemap_url(self, store_url):
        """Generate sitemap URL from store URL"""
        base_url = store_url.rstrip('/')
        return f"{base_url}/sitemap.xml"
    
    def find_contact_page(self, sitemap_url):
        """Find contact page URL from sitemap"""
        try:
            self.driver.get(sitemap_url)
            time.sleep(2)
            
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'xml')
            
            # Find all URLs in sitemap
            urls = soup.find_all('loc')
            
            # Look for contact page
            for url in urls:
                url_text = url.get_text()
                if 'contact' in url_text.lower():
                    return url_text
            
            # If no contact in main sitemap, check sitemap index
            sitemap_links = soup.find_all('sitemap')
            for sitemap in sitemap_links:
                sitemap_loc = sitemap.find('loc')
                if sitemap_loc and 'page' in sitemap_loc.get_text().lower():
                    # Check pages sitemap
                    self.driver.get(sitemap_loc.get_text())
                    time.sleep(1)
                    sub_soup = BeautifulSoup(self.driver.page_source, 'xml')
                    sub_urls = sub_soup.find_all('loc')
                    
                    for url in sub_urls:
                        url_text = url.get_text()
                        if 'contact' in url_text.lower():
                            return url_text
            
            return None
            
        except Exception as e:
            print(f"Error finding contact page: {e}")
            return None
    
    def extract_contact_info(self, contact_url):
        """Extract email and phone from contact page"""
        try:
            self.driver.get(contact_url)
            time.sleep(3)
            
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            emails = set()
            phones = set()
            
            # Find mailto links
            mailto_links = soup.find_all('a', href=re.compile(r'^mailto:'))
            for link in mailto_links:
                email = link['href'].replace('mailto:', '').split('?')[0]
                emails.add(email.strip())
            
            # Find tel links
            tel_links = soup.find_all('a', href=re.compile(r'^tel:'))
            for link in tel_links:
                phone = link['href'].replace('tel:', '').strip()
                phones.add(phone)
            
            # Also search page text for email patterns (backup)
            if not emails:
                email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
                text_emails = re.findall(email_pattern, soup.get_text())
                emails.update(text_emails)
            
            return {
                'emails': list(emails),
                'phones': list(phones)
            }
            
        except Exception as e:
            print(f"Error extracting contact info: {e}")
            return {'emails': [], 'phones': []}
    
    def scrape_store(self, store_url):
        """Scrape contact information from a single store"""
        print(f"\n{'='*60}")
        print(f"Processing: {store_url}")
        print(f"{'='*60}")
        
        # Get sitemap URL
        sitemap_url = self.get_sitemap_url(store_url)
        print(f"Sitemap URL: {sitemap_url}")
        
        # Find contact page
        contact_url = self.find_contact_page(sitemap_url)
        
        if not contact_url:
            print("[X] Contact page not found in sitemap")
            self.results.append({
                'store_url': store_url,
                'contact_url': 'Not found',
                'emails': [],
                'phones': []
            })
            return
        
        print(f"[OK] Contact page found: {contact_url}")
        
        # Extract contact info
        contact_info = self.extract_contact_info(contact_url)
        
        print(f"[EMAIL] Emails found: {contact_info['emails']}")
        print(f"[PHONE] Phones found: {contact_info['phones']}")
        
        self.results.append({
            'store_url': store_url,
            'contact_url': contact_url,
            'emails': contact_info['emails'],
            'phones': contact_info['phones']
        })
    
    def scrape_multiple_stores(self, store_urls):
        """Scrape multiple stores"""
        for url in store_urls:
            try:
                self.scrape_store(url)
            except Exception as e:
                print(f"Error processing {url}: {e}")
        
        self.driver.quit()
    
    def save_to_csv(self, filename='shopify_contacts.csv'):
        """Save results to CSV file"""
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Store URL', 'Contact Page', 'Emails', 'Phone Numbers'])
            
            for result in self.results:
                writer.writerow([
                    result['store_url'],
                    result['contact_url'],
                    ', '.join(result['emails']) if result['emails'] else 'None',
                    ', '.join(result['phones']) if result['phones'] else 'None'
                ])
        
        print(f"\n[OK] Results saved to {filename}")
    
    def print_summary(self):
        """Print summary of results"""
        print(f"\n{'='*60}")
        print("SUMMARY")
        print(f"{'='*60}")
        print(f"Total stores processed: {len(self.results)}")
        
        stores_with_email = sum(1 for r in self.results if r['emails'])
        stores_with_phone = sum(1 for r in self.results if r['phones'])
        
        print(f"Stores with email: {stores_with_email}")
        print(f"Stores with phone: {stores_with_phone}")
        print(f"{'='*60}\n")


# Example usage
if __name__ == "__main__":
    # Add your Shopify store URLs here
    # store_urls = [
    #     "https://redtape.com",
    # "https://jayesh-cirkle.myshopify.com",
    # "https://dte2dc-ra.myshopify.com",
    #     # Add more URLs as needed
    # ]

    with open("sresults_hosts.json", "r", encoding="utf-8") as f:
        store_urls = json.load(f)
    
    print("Shopify Contact Information Scraper")
    print("="*60)
    
    scraper = ShopifyContactScraper()
    scraper.scrape_multiple_stores(store_urls)
    scraper.print_summary()
    scraper.save_to_csv('shopify_contacts.csv')
    
    print("\nDone! Check shopify_contacts.csv for results.")