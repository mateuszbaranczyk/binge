import secrets

from flask import Flask

from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

import routes  # noqa: F401, E402

if __name__ == "__main__":
    app.run(port=6000)
