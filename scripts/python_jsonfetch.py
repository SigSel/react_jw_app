import requests
import json
import argparse
import sys

from typing import List


def parse_args(argument_list: List[str]) -> argparse.Namespace:
    """Parses command line arguments using argparse."""
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--api-key", help="Vinmonopolet open API key")
    return parser.parse_args(argument_list)


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


if __name__ == "__main__":
    main()
