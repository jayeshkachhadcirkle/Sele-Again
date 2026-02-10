import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://www.zomato.com/surat/801-speciality-coffee-more-katargam/order")

html = response.text
# OR: html = driver.page_source (if using Selenium)

soup = BeautifulSoup(html, "html.parser")
print(soup.title.string)

menu = []

# Each category section
category_sections = soup.select("section.sc-bZVNgQ.iGYweR")

for category in category_sections:
    category_name = category.select_one("h4.sc-liPmeQ")
    category_name = category_name.get_text(strip=True) if category_name else ""

    category_desc = category.select_one(".sc-bOxvsH")
    category_desc = category_desc.get_text(strip=True) if category_desc else None

    items = []

    # Each item block
    item_blocks = category.select(".sc-jhLVlY.cFNHph")

    for item in item_blocks:
        name_tag = item.select_one("h4.sc-cdQEHs")
        name = name_tag.get_text(strip=True) if name_tag else ""

        desc_tag = item.select_one("p.sc-fuzEkO")
        desc = desc_tag.get_text(strip=True) if desc_tag else None

        img_tag = item.select_one("img")
        image = img_tag["src"] if img_tag and img_tag.has_attr("src") else None

        if name:
            items.append({
                "name": name,
                "description": desc if desc else None,
                "image": image
            })

    if category_name and items:
        menu.append({
            "categoryName": category_name,
            "description": category_desc,
            "items": items
        })

# Output JSON
print(json.dumps(menu, indent=2, ensure_ascii=False))
