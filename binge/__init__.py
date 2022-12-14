# !/bin/python3
# isort: skip_file
import os
import secrets

from flask import Flask

from flask_session import Session

# enviroment variables
# FLASK_APP=binge
# FLASK_DEBUG=True


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=secrets.token_hex(16),
    )

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    _session = Session()
    _session.init_app(app)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError as err:
        print(err)

    from . import routes

    app.register_blueprint(routes.bp)

    return app
