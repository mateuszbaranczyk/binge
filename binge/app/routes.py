from flask import Flask, render_template, request, redirect
from api_connector import Requester

app = Flask(__name__)
requester = Requester()


@app.route("/")
def main_page():
    # title = request.form['title']

    return render_template("find.html")

@app.route("/title/<title>")
def title_page(title):

    return render_template("title.html", title=title)

