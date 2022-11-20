from api_connector import requester
from flask import redirect, render_template, session, url_for
from forms import PeroidForm, QueryForm
from run import app


fake_data = {
    "title": "Game of Thrones (TV Series 2011–2019)",
    "image": "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_Ratio0.7331_AL_.jpg",
    "description": "desc",
    "seasons": "8",
    "id": "id",
}

fake_duration = 20000


@app.route("/", methods=["GET", "POST"])
def main_page():
    form = QueryForm()
    if form.validate_on_submit():
        title = form.title.data
        # title_id = requester.get_id_by_phrase(phrase=title)
        # title_data = requester.get_title_data(title_id)
        session["title_data"] = fake_data
        return redirect(url_for("title_page"))
    return render_template("home.html", form=form)


@app.route("/title", methods=["GET", "POST"])
def title_page():
    form = PeroidForm()
    title_data = session.get("title_data")
    if form.validate_on_submit():
        # title_duration = requester.get_title_duration(title_data["id"])
        title_duration = fake_duration
        peroid = form.peroid.data
        duration = form.duration.data
        session["message"] = _check_if_can_be_binged(
            int(peroid), int(duration), title_duration
        )
        return redirect(url_for("answer"))
    return render_template("title.html", form=form)


def _check_if_can_be_binged(peroid: int, duration: int, title_duration: int) -> str:
    time_to_binge = duration * peroid
    if title_duration > time_to_binge:
        return "It's impossible!"
    else:
        return "Go ahead, you can make it!"


@app.route("/answer", methods=["GET", "POST"])
def answer():
    return render_template("answer.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
