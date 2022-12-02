import _pytest.skipping
import pytest

from binge import create_app


@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
            "WTF_CSRF_ENABLED": False,
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

#TODO try to use it
# import pytest

# old_skipif = pytest.mark.skipif

# def custom_skipif(*args, **kwargs):
#     return old_skipif(False, reason='disabling skipif')

# pytest.mark.skipif = custom_skipif