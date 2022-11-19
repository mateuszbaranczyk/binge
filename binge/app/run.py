from flask import Flask
import os
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

import routes