from flask import Flask, render_template, request
from api_connector import Requester

app = Flask(__name__)
requester = Requester()


@app.route("/")
def main_page():

    return render_template("find.html")


@app.route("/title")
def title_page():
    return render_template("title.html")
