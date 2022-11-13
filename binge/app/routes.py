from flask import Flask, render_template, request
from api_connector import Requester
from forms import QueryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "twojastara"
requester = Requester()


@app.route("/")
def main_page():
    form = QueryForm()
    return render_template("find.html", title="Binge", form=form)


@app.route("/title")
def title_page():
    return render_template("title.html")
