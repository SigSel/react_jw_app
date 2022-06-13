import undetected_chromedriver as uc
import json


url = "https://www.vinmonopolet.no/api/search?q=:relevance:visibleInSearch:true:mainCategory:brennevin:" \
      "mainSubCategory:brennevin_whisky:mainCountry:japan&searchType=product&currentPage=0&fields=FULL&pageSize=100"


if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument('--headless')
    driver = uc.Chrome(options=options)
    driver.get(url)
    data = driver.page_source.split('pre-wrap;">')[1].split("</pre>")[0]
    data = json.loads(data)

    with open('search.json', 'w') as f:
        json.dump(data, f)
