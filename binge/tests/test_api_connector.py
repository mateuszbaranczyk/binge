from unittest.mock import patch, MagicMock

from binge.app.api_connector import Requester
from binge.tests.testing_responses import (
    SearchSeries_response,
    Title_response,
    SeasonEpisodes_response,
)


def test_get_id_by_phrase():
    with patch("requests.get") as mocked_request:
        mocked_request.return_value.text = str(SearchSeries_response)
        mocked_request.return_value.status_code = 200
        requester = Requester()
        result = requester.get_id_by_phrase("lost")
        assert result == "tt0411008"


def test_get_title_data():
    with patch("requests.get") as mocked_request:
        mocked_request.return_value.text = str(Title_response)
        mocked_request.return_value.status_code = 200
        requester = Requester()
        result = requester.get_title_data("tt0411008")
        assert result == (
            "6",
            "Lost (TV Series 2004–2010)",
            "https://aws.com/img/gole_baby.jpg",
            "null",
        )


def test_get_title_duration():
    pass


@patch("requests.get")
@patch("binge.app.api_connector.Requester.get_title_data")
def test_get_season_duration(get_title_data, mocked_request):
    mocked_request.return_value.text = str(SeasonEpisodes_response)
    mocked_request.return_value.status_code = 200
    get_title_data.return_value = ("3", "full_title", "image", "30")
    requester = Requester()
    result = requester.get_season_duration(title_id="tt0411008", season_number=1)
    assert result == 60


def test_make_request():
    with patch("requests.get") as mocked_request:
        mocked_request.return_value.text = '{"test": "data"}'
        mocked_request.return_value.status_code = 200
        requester = Requester()
        result = requester._make_request("query", "query_params")
        assert result == {"test": "data"}


def test_make_request_with_api_error():
    with patch("requests.get") as mocked_request:
        mocked_request.return_value.status_code = 404
        requester = Requester()
        try:
            result = requester._make_request("query", "query_params")  # noqa: F841
        except AssertionError:
            pass
