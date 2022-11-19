import json
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
        seasons_data = response["tvSeriesInfo"]
        return {
            "seasons": seasons_data["seasons"][-1] if seasons_data else "",
            "title": response["fullTitle"],
            "image": response["image"],
            "duration": response["runtimeMins"],
        }

    def get_title_duration(self, title_id: str, num_seasons: int):
        season = 1
        seasons_duration = []
        while season <= num_seasons:
            seasons_duration.append(self.get_season_duration(title_id, season))
            season += 1
        return sum(seasons_duration)

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
        try:
            return literal_eval(response.text)  # only for testing
        except ValueError:  # TODO fix testing resources
            return json.loads(response.text)
