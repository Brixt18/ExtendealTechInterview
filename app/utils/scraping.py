import json
import re

import requests
from bs4 import BeautifulSoup


class Scraping:
    def __init__(self, uri: str):
        self.uri = uri

        self._html = requests.get(self.uri)
        self.soup = BeautifulSoup(self._html.text, "html.parser")


class Disco(Scraping):
    def __init__(self, uri: str):
        super().__init__(uri)

        self.records = {
            "records": []
        }

    def _get_price(self, dict: dict, data: dict) -> int | None:
        id_price_range = dict.get("priceRange", {}).get("id", "")
        price_range_selling = data.get(id_price_range, {}).get(
            "sellingPrice", {}).get("id", "")
        selling_price = data.get(price_range_selling, {}).get("highPrice")

        return str(selling_price)

    def get_items(self) -> dict:
        """
        Scrap the HTML responses using regex and save the items results in `self.results`

        RETURN
        ------
        A dictionary with the results:
        ```
        {
            "records": list[dict]
        }
        ```
        """
        template_items = [item for item in self.soup.find_all(
            "template", attrs={"data-varname": "__STATE__"})]

        for item in template_items:

            data = re.findall("<script>(.*)<[/]script>", str(item))

            for _data in data:
                _json = json.loads(_data)
                
                for k, v in _json.items():
                    if v.get("brand") is not None:
                        price = self._get_price(v, _json)

                        self.records["records"].append({
                            "marca": v.get("brand"),
                            "decription": v.get("description"),
                            "precio": price
                        })

        return self.records
