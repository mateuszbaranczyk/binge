import pytest

from binge import create_app


@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def session(client):
    def pass_data_to_session(key: str, value: object):
        with client.session_transaction() as session:
            session[key] = value

    return pass_data_to_session
