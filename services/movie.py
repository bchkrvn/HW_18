from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_all_filter(self, year, genre_id, director_id):
        if year:
            all_movies = self.dao.get_by_year(int(year))
        elif director_id:
            all_movies = self.dao.get_by_director(int(director_id))
        elif genre_id:
            all_movies = self.dao.get_by_genre(int(genre_id))
        else:
            all_movies = self.get_all()

        return all_movies

    def get_by_year(self, year: int):
        return self.dao.get_by_year(year)

    def get_by_director(self, d_id):
        return self.dao.get_by_director(d_id)

    def get_by_genre(self, g_id):
        return self.dao.get_by_genre(g_id)

    def get_one(self, id_):
        return self.dao.get_one(id_)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        id_ = data.get('id')
        movie = self.dao.get_one(id_)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def update_partial(self, data):
        id_ = data.get('id')
        movie = self.dao.get_one(id_)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, id_):
        self.dao.delete(id_)