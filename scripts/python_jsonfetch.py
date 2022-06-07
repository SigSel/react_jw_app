import cloudscraper
import json

url = "https://www.vinmonopolet.no/api/search?q=:relevance:visibleInSearch:true:mainCategory:brennevin:" \
      "mainSubCategory:brennevin_whisky:mainCountry:japan&searchType=product&currentPage=0&fields=FULL&pageSize=100"

scraper = cloudscraper.create_scraper()
data = scraper.get(url).text
data = json.loads(data)

with open('search.json', 'w') as f:
    json.dump(data, f)
