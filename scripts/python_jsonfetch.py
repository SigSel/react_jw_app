import requests
import json

url = "https://www.vinmonopolet.no/api/search?q=:relevance:visibleInSearch:true:mainCategory:brennevin:mainSubCategory:brennevin_whisky:mainCountry:japan&searchType=product&currentPage=0&fields=FULL&pageSize=100"
headers = {
    'User-Agent':
        'python_requests',
    'Content-Type':
        'application/json; charset=utf-8'
}

resp = requests.get(url=url, headers=headers)
print(resp.status_code)
data = json.loads(resp.text)

with open('search.json', 'w') as f:
    json.dump(data, f)
