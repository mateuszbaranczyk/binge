from binge import database
from tests.testing_api_responses import title_data
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
operations = database.Operations()


def test_add_title_data_to_db(app_context):
    operations.save_title(title_data=title_data)
    result = db.get_or_404(database.TitleData, title_data["id"])
    assert result is not None
