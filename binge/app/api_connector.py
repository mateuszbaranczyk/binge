import os
from ast import literal_eval

import requests

# TODO api errors handling


class Requester:
    def __init__(self):
        self.url = "https://imdb-api.com/en/API/"
        self.api_key = os.getenv("IMDB_API_KEY")

    def get_id_by_phrase(self, phrase: str) -> str:
        query = "SearchSeries"
        url = f"{self.url}/{query}/{self.api_key}/{phrase}"
        response = requests.get(url=url).text
        best_match = literal_eval(response)["results"][0]
        return best_match["id"]

    def get_single_episode(self):
        pass
