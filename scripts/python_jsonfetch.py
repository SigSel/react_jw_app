import json
from playwright.sync_api import sync_playwright


url = "https://www.vinmonopolet.no/api/search?q=:relevance:visibleInSearch:true:mainCategory:brennevin:" \
      "mainSubCategory:brennevin_whisky:mainCountry:japan&searchType=product&currentPage=0&fields=FULL&pageSize=100"

with sync_playwright() as p:
    # Webkit is fastest to start and hardest to detect
    browser = p.webkit.launch(headless=True)

    page = browser.new_page()
    page.goto(url)

    # Use evaluate instead of `content` not to import bs4 or lxml
    html = page.evaluate('document.querySelector("pre").innerText')


data = json.loads(html)

with open('search.json', 'w') as f:
    json.dump(data, f)
