import requests
import json
import argparse
import sys
import pandas

from typing import List


def parse_args(argument_list: List[str]) -> argparse.Namespace:
    """Parses command line arguments using argparse."""
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--api-key", help="Vinmonopolet open API key")
    return parser.parse_args(argument_list)


def create_csv_file(json_path: str, csv_path: str) -> None:
    df = pd.read_json(json_path)

    data = pd.DataFrame(df["productSearchResult"]["products"])
    keep = ["code", "name", "url", "product_selection", "price", "volume", "images"]
    data = data.filter(items=keep)
    data["price"] = pd.json_normalize(data["price"])["formattedValue"]
    data["images"] = pd.json_normalize(pd.json_normalize(data["images"])[1])["url"]
    data["volume"] = pd.json_normalize(data["volume"])["value"]
    data.to_csv(csv_path)


def main() -> None:

    args = parse_args(sys.argv[1:])
    url = "https://www.vinmonopolet.no/api/search?q=:relevance:visibleInSearch:true:mainCategory:brennevin:" \
          "mainSubCategory:brennevin_whisky:mainCountry:japan&searchType=product&currentPage=0&fields=FULL&pageSize=100"
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': args.api_key
    }

    resp = requests.get(url=url, headers=headers)
    print(resp.status_code)
    data = resp.json()

    with open('search.json', 'w') as f:
        json.dump(data, f)
    
    create_csv_file(json_path="search.json", csv_path="src/JW_vinmon.csv")


if __name__ == "__main__":
    main()
