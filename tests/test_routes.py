from binge import create_app
from tests.testing_api_responses import standard_result
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
    session_data = session("title_data", standard_result)
    response = client.get("/title")
    result = response.data.decode("utf-8")
    assert standard_result["title"] in result
    assert standard_result["image"] in result
    assert standard_result["description"] in result
