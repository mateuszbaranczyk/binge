from binge import db
from tests.testing_api_responses import title_data
from binge import database
import pytest

operations = database.Operations()


@pytest.fixture(autouse=True)
def setup_andteardown(app_context):
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()

def test_add_title_data_to_db(app_context):
    operations.save_title(title_data=title_data)
    result = db.get_or_404(database.TitleData, title_data["id"])
    assert result.title == title_data["title"]

