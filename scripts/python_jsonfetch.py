import requests
import json
import argparse
import sys
import pandas as pd

from typing import List, Optional


class ProductFetcher:
    def __init__(self, api_key: str, csv_path: str):
        self.api_key: str = api_key
        self.csv_path: str = csv_path
        self.data_frames: List[Optional[pd.DataFrame]] = []

    def _add_json_to_dataframe(self, json_path: str) -> bool:
        found_valid_data = True
        df = pd.read_json(json_path)

        data = pd.DataFrame(df["productSearchResult"]["products"])
        keep = ["code", "name", "url", "product_selection", "price", "volume", "images"]
        try:
            data = data.filter(items=keep)
            data["price"] = pd.json_normalize(data["price"])["formattedValue"]
            data["images"] = pd.json_normalize(pd.json_normalize(data["images"])[1])["url"]
            data["volume"] = pd.json_normalize(data["volume"])["value"]
            self.data_frames.append(data)
        except KeyError:
            found_valid_data = False

        return found_valid_data

    def _create_csv(self) -> None:
        combined_data = pd.concat(self.data_frames, ignore_index=True)
        combined_data.to_csv(self.csv_path)

    def _make_api_request(self, page_number: int) -> bool:
        url = "https://www.vinmonopolet.no/vmpws/v2/vmp/search?q=:relevance:mainCategory:brennevin:mainCountry:japan" \
              f":mainSubCategory:brennevin_whisky&searchType=product&currentPage={page_number}&fields=FULL&pageSize=24"
        headers = {
            'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': self.api_key
        }

        resp = requests.get(url=url, headers=headers)
        print(resp.status_code)
        data = resp.json()

        json_path = f"search{page_number}.json"
        with open(json_path, 'w') as f:
            json.dump(data, f)

        return self._add_json_to_dataframe(json_path=json_path)

    def fetch_data(self, number_of_pages: int = 10) -> None:
        for page_number in range(number_of_pages):
            found_data_on_page = self._make_api_request(page_number=page_number)
            if not found_data_on_page:
                break

        self._create_csv()


def parse_args(argument_list: List[str]) -> argparse.Namespace:
    """Parses command line arguments using argparse."""
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--api-key", help="Vinmonopolet open API key")
    return parser.parse_args(argument_list)


def main() -> None:
    args = parse_args(sys.argv[1:])
    fetcher = ProductFetcher(api_key=args.api_key, csv_path="../src/JW_vinmon.csv")
    fetcher.fetch_data(number_of_pages=10)


if __name__ == "__main__":
    main()
