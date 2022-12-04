from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TitleData(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    image = db.Column(db.String)
    seasons = db.Column(db.String)
    duration = db.Column(db.String, nullable=True)
