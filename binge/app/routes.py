from flask import Flask, render_template, request, redirect, url_for, flash
from api_connector import Requester
from forms import QueryForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "twojastara"
requester = Requester()


@app.route("/", methods=["GET", "POST"])
def main_page():
    form = QueryForm()
    if form.validate_on_submit():
        title = form.title.data
        return redirect(url_for("title_page", title=title))
    return render_template("find.html", form=form)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/title", methods=["GET", "POST"])
def title_page():
    # title = request.args.get("title")
    # title_id = requester.get_id_by_phrase(phrase=title)
    # response = requester.get_title_data(title_id)
    response = (
        "8",
        "Game of Thrones (TV Series 2011–2019)",
        "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_Ratio0.7331_AL_.jpg",
        None,
    )
    title_data = {
        "title": response[1],
        "image": response[2],
        "seasons": response[0],
        "description": "some dummy desc",
    }

    return render_template("title.html", title_data=title_data)
