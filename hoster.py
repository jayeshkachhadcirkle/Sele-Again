import json
from urllib.parse import urlparse

def to_host_only(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url.lstrip("/")

    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"


# load file
with open("search_results.json", "r", encoding="utf-8") as f:
    urls = json.load(f)

# convert
hosts = list(dict.fromkeys(to_host_only(url) for url in urls))  # removes duplicates

# save
with open("sresults_hosts.json", "w", encoding="utf-8") as f:
    json.dump(hosts, f, indent=2)

print("Done > sresults_hosts.json")
