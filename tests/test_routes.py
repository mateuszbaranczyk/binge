from binge import create_app
from tests.testing_api_responses import title_data

# black/isort conflict
# fmt: off
from tests.testing_endpoint_responses import home_form_btn, home_form_field

# fmt: on


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
