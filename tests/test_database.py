from binge.database import Operations as db
from tests.testing_api_responses import title_data

def test_add_title_data_to_db(app_context):
    db.save_title(title_data=title_data)

