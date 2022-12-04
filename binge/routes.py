from flask import Blueprint, redirect, render_template, session, url_for

from binge.api_connector import Requester
from binge.forms import PeroidForm, QueryForm

bp = Blueprint("routes", __name__)
requester = Requester()

@bp.route("/", methods=["GET", "POST"])
def main_page():
    form = QueryForm(prefix="form")
    if form.validate_on_submit():
        _get_title_data(form=form)
        return redirect(url_for("routes.title_page"))
    return render_template("home.html", form=form)


def _get_title_data(form: QueryForm) -> None:
    title = form.title.data
    title_id = requester.get_id_by_phrase(phrase=title)
    session["title_data"] = requester.get_title_data(title_id)
    return None


@bp.route("/title", methods=["GET", "POST"])
def title_page():
    form = PeroidForm(prefix="form")
    title_data = session.get("title_data")
    if form.validate_on_submit():
        _create_message(form=form, title_data=title_data)
        return redirect(url_for("routes.answer"))
    return render_template("title.html", form=form, title_data=title_data)


def _create_message(form: PeroidForm, title_data: dict) -> None:
    title_duration = requester.get_title_duration(
        title_data["id"], int(title_data["seasons"])
    )
    peroid = int(form.peroid.data)
    duration = int(form.duration.data)
    session["message"] = _check_if_can_be_binged(
        peroid, duration, title_duration
    )
    return None


def _check_if_can_be_binged(peroid: int, duration: int, title_duration: int) -> str:
    time_to_binge = duration * peroid
    if title_duration > time_to_binge:
        return "It's impossible!"
    else:
        return "Go ahead, you can make it!"


@bp.route("/answer", methods=["GET", "POST"])
def answer():
    message = session["message"]
    return render_template("answer.html", message=message)


@bp.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
