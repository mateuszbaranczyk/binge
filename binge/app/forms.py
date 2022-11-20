from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    title = StringField(
        "Title", validators=[DataRequired()], render_kw={"placeholder": "Teletubbies"}
    )
    find_it = SubmitField()


class PeroidForm(FlaskForm):
    minutes_in_day = 1440

    duration = StringField(
        "Requested duration",
        validators=[DataRequired()],
        render_kw={"placeholder": "7"},
        default="7",
    )
    peroid = SelectField(
        "Peroid",
        choices=[
            (minutes_in_day, "days"),
            (minutes_in_day * 7, "weeks"),
            (minutes_in_day * 30, "months"),
        ],
        default="days",
    )
    go = SubmitField()
