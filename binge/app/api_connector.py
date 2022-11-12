import os
from ast import literal_eval
from typing import Tuple

import requests


class Requester:
    def __init__(self):
        self.url = "https://imdb-api.com/en/API"
        self.api_key = os.getenv("IMDB_API_KEY")

    def get_id_by_phrase(self, phrase: str) -> str:
        response = self._make_request(query="SearchSeries", query_params=phrase)
        best_match = response["results"][0]["id"]
        return best_match

    def get_title_data(self, title_id: str) -> Tuple[str, str, str, str]:
        response = self._make_request(query="Title", query_params=title_id)
        num_seasons = response["tvSeriesInfo"]["seasons"][-1]
        full_title = response["fullTitle"]
        image = response["image"]
        runtime = response["runtimeMins"]
        return num_seasons, full_title, image, runtime

    def get_title_duration(self, title_id: str, num_seasons: int):
        pass

    def get_season_duration(self, title_id: str, season_number: int) -> int:
        response = self._make_request(
            query="SeasonEpisodes", query_params=f"{title_id}/{season_number}"
        )
        episodes_id = [episode["id"] for episode in response["episodes"]]
        runtimes = [self.get_title_data(episode)[-1] for episode in episodes_id]
        runtimes = [int(episode_runtime) for episode_runtime in runtimes]
        return sum(runtimes)

    def _make_request(self, query: str, query_params: str) -> dict:
        path = f"{self.url}/{query}/{self.api_key}/{query_params}"
        response = requests.get(path)
        assert response.status_code == 200
        return literal_eval(response.text)
