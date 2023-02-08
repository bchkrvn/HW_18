from dao.models.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, id_: int):
        return self.session.query(Movie).get(id_)

    def get_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_by_director(self, d_id):
        return self.session.query(Movie).filter(Movie.director_id == d_id).all()

    def get_by_genre(self, g_id):
        return self.session.query(Movie).filter(Movie.genre_id == g_id).all()

    def create(self, data: dict):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie: Movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, id_: int):
        movie = self.get_one(id_)
        self.session.delete(movie)
        self.session.commit()
