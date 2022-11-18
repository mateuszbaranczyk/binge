from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    title = StringField(
        "Title", validators=[DataRequired()], render_kw={"placeholder": "Teletubbies"}
    )


class PeroidForm(FlaskForm):
    duration = StringField(
        "Requested duration",
        validators=[DataRequired()],
        render_kw={"placeholder": "7"},
        default="7",
    )
    peroid = SelectField("Peroid", choices=["days", "weeks", "months"], default="days")
    go = SubmitField()
