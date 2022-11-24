from binge import create_app
from tests.testing_api_responses import title_data
from tests.testing_endpoint_responses import home_form_btn, home_form_field
from unittest.mock import MagicMock, patch
from binge.routes import _redirect_to_answer_page, _check_if_can_be_binged


def test_render_home_page(client):
    response = client.get("/")
    assert b"What series do you want to binge?" in response.data
    assert home_form_btn in response.data
    assert home_form_field in response.data


def test_render_title_page(client, session):
    session_data = session("title_data", title_data)
    response = client.get("/title")
    result = response.data.decode("utf-8")
    assert title_data["title"] in result
    assert title_data["image"] in result
    assert title_data["description"] in result


def test_render_anser_page(client, session):
    expected_result = "test msg"
    session_data = session("message", expected_result)
    response = client.get("/answer")
    assert expected_result in response.data.decode("utf-8")


@patch("requester.get_title_duration")
def test_redirect_to_answer_page(get_title_duration):
    get_title_duration.return_value = 12
    form = create_form(peroid="1", duration="24")
    _redirect_to_answer_page(form)


def _create_form(peroid: str, duration: str) -> object:
    form = MagicMock()
    form.return_value.peroid.data = peroid
    form.return_value.duration.data = duration
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
