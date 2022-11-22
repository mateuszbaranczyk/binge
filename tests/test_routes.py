from binge import create_app

# black/isort conflict
# fmt: off
from tests.testing_endpoint_responses import home_form_btn, home_form_field
# fmt: on


def test_render_home_page(client):
    response = client.get("/")
    assert b"What series do you want to binge?" in response.data
    assert home_form_btn in response.data
    assert home_form_field in response.data
