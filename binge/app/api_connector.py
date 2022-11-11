import os

import requests

url = "https://imdb-api.com/en/API"
query = "SearchSeries"
api_key = os.getenv("IMDB_API_KEY")
expression = "lost"

path = f"{url}/{query}/{api_key}/{expression}"

result = requests.request("GET", path)


class Requester:
    def __init__(self):
        self.url = "https://imdb-api.com/en/API/"
        self.api_key = os.getenv("IMDB_API_KEY")

    def get_id_by_phrase(self, phrase:str) -> str:
        query = "SearchSeries"
        url = f"{self.url}/{query}/{self.api_key}/{phrase}"
        response = requests.get(url=url)
        response = response.text
        return response

    def get_single_episode(self):
        pass
