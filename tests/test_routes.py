from unittest.mock import MagicMock, patch

import pytest

from binge import create_app
from binge.forms import PeroidForm
from binge.routes import _check_if_can_be_binged, _redirect_to_answer_page
from tests.testing_api_responses import title_data
from tests.testing_endpoint_responses import home_form_btn, home_form_field


def test_render_home_page(client):
    response = client.get("/")
    assert b"What series do you want to binge?" in response.data
    assert home_form_btn in response.data
    assert home_form_field in response.data


def test_render_title_page(client, session):
    session(title_data=title_data)
    response = client.get("/title")
    result = response.data.decode("utf-8")
    assert title_data["title"] in result
    assert title_data["image"] in result
    assert title_data["description"] in result


def test_render_answer_page(client, session):
    expected_result = "test msg"
    session(message=expected_result)
    response = client.get("/answer")
    assert expected_result in response.data.decode("utf-8")


@patch("binge.api_connector.requester.get_title_duration")
def test_redirect_to_answer_page(get_title_duration, app, session):
    title_data = {"id": "test_id", "seasons": "1"}
    session(title_data=title_data)
    get_title_duration.return_value = 12
    form = _create_form(peroid="1", duration="24")
    with app.test_request_context("/title", form=PeroidForm(), title_data=title_data):
        _redirect_to_answer_page(form, title_data)


def _create_form(peroid: str, duration: str) -> object:
    form = MagicMock()
    form.peroid.data.return_value = peroid
    form.duration.data.return_value = duration
    return form


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
