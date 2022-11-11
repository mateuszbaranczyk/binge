import os
from ast import literal_eval

import requests

# TODO api errors handling


class Requester:
    def __init__(self):
        self.url = "https://imdb-api.com/en/API"
        self.api_key = os.getenv("IMDB_API_KEY")

    def get_id_by_phrase(self, phrase: str) -> str:
        query = "SearchSeries"
        url = f"{self.url}/{query}/{self.api_key}/{phrase}"
        response = requests.get(url=url).text
        best_match = literal_eval(response)["results"][0]
        return best_match["id"]

    def get_title_data(self, title_id: str) -> Tuple[str, str, str]:
        query = "Title"
        url = f"{self.url}/{query}/{self.api_key}/{title_id}"
        response = requests.get(url=url).text
        response = literal_eval(response)
        num_seasons = response["tvSeriesInfo"]["seasons"][-1]
        full_title = response["fullTitle"]
        image = response["image"]
        return (num_seasons, full_title, image)
