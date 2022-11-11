from unittest.mock import patch

from binge.app.api_connector import Requester
from binge.tests.testing_responses import SearchSeries_api_response


def test_get_id_by_phrase():
    with patch("requests.get") as mocked_request:
        mocked_request.return_value.text = str(SearchSeries_api_response)
        requester = Requester()
        result = requester.get_id_by_phrase("lost")
        assert result == "tt0411008"
