from dao.models.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, id_: int):
        return self.session.query(Genre).get(id_)

    def create(self, data: dict):
        new_movie = Genre(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie: Genre):
        self.session.add(movie)
        self.session.commit()

    def delete(self, id_: int):
        movie = self.get_one(id_)
        self.session.delete(movie)
        self.session.commit()
