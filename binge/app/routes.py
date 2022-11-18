from api_connector import Requester
from flask import Flask, redirect, render_template, request, url_for
from forms import PeroidForm, QueryForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "twojastara"
requester = Requester()

fake_data = (
    "8",
    "Game of Thrones (TV Series 2011–2019)",
    "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_Ratio0.7331_AL_.jpg",
    None,
)


@app.route("/", methods=["GET", "POST"])
def main_page():
    form = QueryForm()
    if form.validate_on_submit():
        title = form.title.data
        return redirect(url_for("title_page", title=title))
    return render_template("find.html", form=form)


@app.route("/title", methods=["GET", "POST"])
def title_page():
    form = PeroidForm()
    # title = request.args.get("title")
    # title_id = requester.get_id_by_phrase(phrase=title)
    # response = requester.get_title_data(title_id)

    title_data = {
        "title": fake_data[1],
        "image": fake_data[2],
        "seasons": fake_data[0],
        "description": "some dummy desc",
    }
    if form.validate_on_submit():
        peroid = form.peroid.data
        duration = form.duration.data
        return redirect(url_for("answer", peroid=peroid, duration=duration))
    return render_template("title.html", title_data=title_data, form=form)


@app.route("/answer", methods=["GET", "POST"])
def answer():
    peroid = request.args.get("peroid")
    duration = request.args.get("duration")

    return render_template("answer.html", peroid=peroid, duration=duration)


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
