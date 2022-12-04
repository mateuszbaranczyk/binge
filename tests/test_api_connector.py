from unittest.mock import patch

import pytest

from binge.api_connector import Requester
from tests import testing_api_responses as api


@patch("requests.get")
def test_get_id_by_phrase(mocked_request):
    mocked_request.return_value.text = str(api.SearchSeries_response)
    mocked_request.return_value.status_code = 200
    requester = Requester()
    result = requester.get_id_by_phrase("lost")
    assert result == "tt0411008"


@pytest.mark.parametrize(
    "input,expected_result",
    [
        (
            api.Title_response,
            api.title_data,
        ),
        (
            api.Title_response_without_seasons,
            api.result_without_seasons,
        ),
    ],
)
@patch("requests.get")
def test_get_api_title_data(mocked_request, input, expected_result):
    mocked_request.return_value.text = str(input)
    mocked_request.return_value.status_code = 200
    requester = Requester()
    result = requester.get_title_data("tt0411008")
    assert result == expected_result


@patch("binge.api_connector.Requester.get_season_duration")
def test_get_title_duration(get_season_duration):
    get_season_duration.return_value = 60
    requester = Requester()
    result = requester.get_title_duration(title_id="tt0411008", num_seasons=2)
    assert result == 120


@pytest.mark.parametrize("num_seasons", [1, 2, 3])
@patch("requests.get")
@patch("binge.api_connector.Requester.get_title_data")
def test_get_season_duration(get_title_data, mocked_request, num_seasons):
    mocked_request.return_value.text = str(api.SeasonEpisodes_response)
    mocked_request.return_value.status_code = 200
    get_title_data.return_value = ("3", "full_title", "image", "30")
    requester = Requester()
    result = requester.get_season_duration(
        title_id="tt0411008", season_number=num_seasons
    )
    assert result == 60


@patch("requests.get")
def test_make_request(mocked_request):
    mocked_request.return_value.text = '{"test": "data"}'
    mocked_request.return_value.status_code = 200
    requester = Requester()
    result = requester._make_request("query", "query_params")
    assert result == {"test": "data"}


@patch("requests.get")
def test_make_request_rises_error_with_bad_request(mocked_request):
    mocked_request.return_value.status_code = 404
    requester = Requester()
    try:
        requester._make_request("query", "query_params")
    except AssertionError:
        pass


@pytest.mark.skip(reason="limited acces to api")
def test_requester():
    requester = Requester()
    title_id = requester.get_id_by_phrase("House of the Dragon")
    api.title_data = requester.get_api.title_data(title_id)
    title_duration = requester.get_title_duration(
        title_id, int(api.title_data["seasons"])
    )
    assert title_duration == 615
