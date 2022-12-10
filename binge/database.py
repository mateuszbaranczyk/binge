from binge import db


class TitleData(db.Model):
    title_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    image = db.Column(db.String)
    seasons = db.Column(db.String)
    duration = db.Column(db.String, nullable=True)


class Operations:
    def __init__(self):
        self.db = db

    def save_title(self, title_data: dict) -> None:
        data_to_commit = TitleData(
            title_id=title_data["id"],
            title=title_data["title"],
            description=title_data["description"],
            image=title_data["image"],
            seasons=title_data["seasons"],
            duration=title_data["duration"],
        )
        self.db.session.add(data_to_commit)
        self.db.session.commit()
        # TODO logging
        return None

    def get_title(self, id: str) -> dict:
        title = session.get(TitleData, id)
        db.get()
        return title.__dict__

    def update_title(self, id: str, **kwargs):
        title = db.get_or_404(TitleData, id)
        for key, value in kwargs:
            setattr(title, key, value)

    def genearate_thumbnail(self):
        pass
