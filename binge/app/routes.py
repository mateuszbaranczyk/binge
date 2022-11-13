from flask import Flask, render_template
from api_connector import Requester

app = Flask(__name__)
requester = Requester()



@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/<title>")
def show_title_page(title: str):
    pass