from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TitleData(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    image = db.Column(db.String)
    seasons = db.Column(db.String)
    duration = db.Column(db.String, nullable=True)


class Operations:
    def __init__(self):
        pass

    def save_title(self, title_data: dict) -> None:
        data_to_commit = TitleData(
            id=title_data["id"],
            title=title_data["title"],
            descriptrion=title_data["description"],
            image=title_data["image"],
            seasons=title_data["seasons"],
            duration=title_data["duration"],
        )
        db.add(data_to_commit)
        db.commit()
        # TODO logging
        return None

    def get_title(self, id: str) -> dict:
        title = db.get(TitleData, id)
        db.get()
        return title.__dict__

    def update_title(self, id: str, **kwargs):
        title = db.get_or_404(TitleData, id)
        for key, value in kwargs:
            setattr(title, key, value)

    def genearate_thumbnail(self):
        pass
