from binge.requester.api_connector import Requester
from unittest.mock import MagicMock

SearchSeries_api_response = result = '{"searchType":"Series","expression":"lost","results":[{"id":"tt0411008","resultType":"Title","image":"https://m.media-amazon.com/images/M/MV5BNzhlY2E5NDUtYjJjYy00ODg3LWFkZWQtYTVmMzU4ZWZmOWJkXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_Ratio0.7273_AL_.jpg","title":"Lost","description":"(2004) (TV Series)"},{"id":"tt14609588","resultType":"Title","image":"https://m.media-amazon.com/images/M/MV5BMmU5ZTRmZmEtYjA1Ny00NzRlLWIyODItZWQ4NDlkYzFmNDYyXkEyXkFqcGdeQXVyNDY5MjMyNTg@._V1_Ratio0.7273_AL_.jpg","title":"Lost","description":"(2021) (TV Series)"},{"id":"tt5232792","resultType":"Title","image":"https://m.media-amazon.com/images/M/MV5BZTY5YjQwYmEtOWJiNy00NDBmLTgxM2YtMmVkMmI0NzE1N2FjXkEyXkFqcGdeQXVyMjg1NDcxNDE@._V1_Ratio0.7273_AL_.jpg","title":"Lost in Space","description":"(2018) (TV Series)"},{"id":"tt11379026","resultType":"Title","image":"https://m.media-amazon.com/images/M/MV5BMzRlOTdiNGEtOTlmZi00YjNiLTljZjItZGNhNjY5ZDM4Yzg2XkEyXkFqcGdeQXVyNjc0MjkzNjc@._V1_Ratio0.7273_AL_.jpg","title":"Ghosts","description":"(2021) (TV Series)"}],"errorMessage":""}'

def test_get_id_by_phrase():
    api = MagicMock()
    api.text.return_value = SearchSeries_api_response

