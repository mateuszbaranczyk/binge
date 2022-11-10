import requests
import os

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

    def get_id_by_phrase(self, phrase):
        pass

    def get_single_episode(self):
        pass

