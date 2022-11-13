from flask import Flask, render_template, request, redirect, url_for, flash
from api_connector import Requester
from forms import QueryForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "twojastara"
requester = Requester()


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = QueryForm()
    if form.validate_on_submit():
        title = form.title.data
        return redirect(url_for("title_page", title=title))
    return render_template('find.html', form=form)


@app.route('/title', methods=['GET', 'POST'])
def title_page():
    return render_template("title.html")
