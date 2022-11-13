from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired

class QueryForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
