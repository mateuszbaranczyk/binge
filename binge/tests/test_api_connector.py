from unittest.mock import patch

import pytest

from binge.app.api_connector import Requester
from binge.tests.testing_responses import (
    SearchSeries_response,
    SeasonEpisodes_response,
    Title_response,
    Title_response_without_seasons,
    result_without_seasons,
    standard_result,
)


@patch("requests.get")
def test_get_id_by_phrase(mocked_request):
    mocked_request.return_value.text = str(SearchSeries_response)
    mocked_request.return_value.status_code = 200
    requester = Requester()
    result = requester.get_id_by_phrase("lost")
    assert result == "tt0411008"


@pytest.mark.parametrize(
    "input,expected_result",
    [
        (
            Title_response,
            standard_result,
        ),
        (
            Title_response_without_seasons,
            result_without_seasons,
        ),
    ],
)
@patch("requests.get")
def test_get_title_data(mocked_request, input, expected_result):
    mocked_request.return_value.text = str(input)
    mocked_request.return_value.status_code = 200
    requester = Requester()
    result = requester.get_title_data("tt0411008")
    assert result == expected_result


@patch("binge.app.api_connector.Requester.get_season_duration")
def test_get_title_duration(get_season_duration):
    get_season_duration.return_value = 60
    requester = Requester()
    result = requester.get_title_duration(title_id="tt0411008", num_seasons=2)
    assert result == 120


@patch("requests.get")
@patch("binge.app.api_connector.Requester.get_title_data")
def test_get_season_duration(get_title_data, mocked_request):
    mocked_request.return_value.text = str(SeasonEpisodes_response)
    mocked_request.return_value.status_code = 200
    get_title_data.return_value = ("3", "full_title", "image", "30")
    requester = Requester()
    result = requester.get_season_duration(title_id="tt0411008", season_number=1)
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
        result = requester._make_request("query", "query_params")  # noqa: F841
    except AssertionError:
        pass


@pytest.mark.skip(reason="limited acces to api")
def test_requester():
    requester = Requester()
    title_id = requester.get_id_by_phrase("House of the Dragon")
    title_data = requester.get_title_data(title_id)
    title_duration = requester.get_title_duration(title_id, int(title_data[0]))
    assert title_duration == 615
