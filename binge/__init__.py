import secrets
import os

from flask import Flask, session

from flask_session import Session
import secrets

#enviroment variables 
# FLASK_APP=binge
# FLASK_ENV=development

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=secrets.token_hex(16),
        SESSION_PERMANENT=False,
        SESSION_TYPE="filesystem"
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        print("OSError")

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app