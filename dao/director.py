from dao.models.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, id_: int):
        return self.session.query(Director).get(id_)

    def create(self, data: dict):
        new_movie = Director(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie: Director):
        self.session.add(movie)
        self.session.commit()

    def delete(self, id_: int):
        movie = self.get_one(id_)
        self.session.delete(movie)
        self.session.commit()
