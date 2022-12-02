from unittest.mock import MagicMock, patch

import pytest

from binge import create_app
from binge.forms import PeroidForm

# black/isort conflict
# fmt: off
from binge.routes import (_check_if_can_be_binged, _create_message,
                          _get_title_data)
# fmt: on
from tests.testing_api_responses import title_data
from tests.testing_endpoint_responses import home_form_btn, home_form_field


def test_render_home_page(client):
    response = client.get("/")
    assert b"What series do you want to binge?" in response.data
    assert home_form_btn in response.data
    assert home_form_field in response.data


@patch("binge.api_connector.requester.get_id_by_phrase")
@patch("binge.api_connector.requester.get_title_data")
def test_add_title_data_to_session(get_id_by_phrase, get_title_data, client):
    get_id_by_phrase.return_value = "ID"
    get_title_data.return_value = title_data
    with client:
        client.post("/", data={"form-title": "title"})

    assert redirect.status_code == 302
    assert redirect.location == "/title"


def test_render_title_page(client, session):
    session(title_data=title_data)
    response = client.get("/title")
    result = response.data.decode("utf-8")
    assert title_data["title"] in result
    assert title_data["image"] in result
    assert title_data["description"] in result


def test_render_answer_page(client, session):
    expected_result = b"test msg"
    session(message=expected_result)
    response = client.get("/answer")
    assert expected_result in response.data


@patch("binge.api_connector.requester.get_title_duration")
def test_add_message_to_session(get_title_duration, client, session):
    get_title_duration.return_value = 12
    with client:
        client.get("/title")
        form = _create_peroid_form(peroid="1", duration="24")
        _create_message(form=form, title_data={"id": "11", "seasons": "22"})
        message = session["message"]
    assert redirect.status_code == 302
    assert redirect.location == "/answer"


@pytest.mark.parametrize(
    "peroid, duration, title_duration, expected_result",
    [
        (1, 24, 12, "Go ahead, you can make it!"),
        (1, 24, 24, "Go ahead, you can make it!"),
        (1, 24, 50, "It's impossible!"),
    ],
)
def test__check_if_can_be_binged(peroid, duration, title_duration, expected_result):
    result = _check_if_can_be_binged(peroid, duration, title_duration)
    assert result == expected_result


def _create_query_form(title) -> "mocked_form":
    mocked_form = MagicMock()
    mocked_form.return_value.title.data = title
    return mocked_form


def _create_peroid_form(peroid: str, duration: str) -> "mocked_form":
    mocked_form = MagicMock()
    mocked_form.return_value.peroid.data = peroid
    mocked_form.return_value.duration.data = duration
    return mocked_form
