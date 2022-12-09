from flask_sqlalchemy import model, Column, String, Text, session



class TitleData(model.Model):
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(Text)
    image = Column(String)
    seasons = Column(String)
    duration = Column(String, nullable=True)


class Operations:
    def __init__(self):
        pass

    def save_title(self, title_data: dict) -> None:
        data_to_commit = TitleData(
            id=title_data["id"],
            title=title_data["title"],
            description=title_data["description"],
            image=title_data["image"],
            seasons=title_data["seasons"],
            duration=title_data["duration"],
        )
        session.add(data_to_commit)
        session.commit()
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
