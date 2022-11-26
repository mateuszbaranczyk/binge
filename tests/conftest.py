import _pytest.skipping
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
    def pass_data_to_session(**kwargs):
        with client.session_transaction() as session:
            for key in kwargs:
                session[key] = kwargs[key]

    return pass_data_to_session


def pytest_addoption(parser):
    parser.addoption(
        "--no-skips", action="store_true", default=False, help="disable skip marks"
    )


@pytest.hookimpl(tryfirst=True)
def pytest_cmdline_preparse(config, args):
    if "--no-skips" not in args:
        return

    def no_skip(*args, **kwargs):
        return

    _pytest.skipping.skip = no_skip
