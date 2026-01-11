import requests
from bs4 import BeautifulSoup

html_content = "";
with open("z0.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())

div = soup.find(class_="sc-bFADNz euONpu")

print(div)