from flask import Blueprint, redirect, render_template, session, url_for

from binge.api_connector import requester
from binge.forms import PeroidForm, QueryForm

bp = Blueprint("routes", __name__)


@bp.route("/", methods=["GET", "POST"])
def main_page():
    form = QueryForm()
    if form.validate_on_submit():
        title = form.title.data
        title_id = requester.get_id_by_phrase(phrase=title)
        title_data = requester.get_title_data(title_id)
        session["title_data"] = title_data
        return redirect(url_for("routes.title_page"))
    return render_template("home.html", form=form)


@bp.route("/title", methods=["GET", "POST"])
def title_page():
    form = PeroidForm()
    title_data = session.get("title_data")
    if form.validate_on_submit():
        _redirect_to_answer_page(form)
    return render_template("title.html", form=form, title_data=title_data)


def _redirect_to_answer_page(form):
    title_duration = requester.get_title_duration(
        title_data["id"], int(title_data["seasons"])
    )
    title_duration = title_duration
    peroid = form.peroid.data
    duration = form.duration.data
    session["message"] = _check_if_can_be_binged(   
        int(peroid), int(duration), title_duration
    )
    return redirect(url_for("answer"))


def _check_if_can_be_binged(peroid: int, duration: int, title_duration: int) -> str:
    time_to_binge = duration * peroid
    if title_duration > time_to_binge:
        return "It's impossible!"
    else:
        return "Go ahead, you can make it!"


@bp.route("/answer", methods=["GET", "POST"])
def answer():
    return render_template("answer.html", message=session["message"])


@bp.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
