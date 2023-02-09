from dao.movie import MovieDAO


class MovieService:
    """
    Класс для связи view и dao
    """
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self) -> list:
        """
        Получить все фильмы из БД
        :return: list
        """
        return self.dao.get_all()

    def get_all_filter(self, year: int, genre_id: int, director_id: int) -> list:
        """
        Получить фильмы по году, жанру или режиссеру
        :param year: год выпуска
        :param genre_id: id жанра
        :param director_id: id режиссера
        :return: list
        """
        if year:
            all_movies = self.dao.get_by_year(int(year))
        elif director_id:
            all_movies = self.dao.get_by_director(int(director_id))
        elif genre_id:
            all_movies = self.dao.get_by_genre(int(genre_id))
        else:
            all_movies = self.get_all()

        return all_movies

    def get_one(self, id_: int):
        """
        Получить фильм по его id
        :param id_: id фильма
        :return: объект класса Movie
        """
        return self.dao.get_one(id_)

    def create(self, data: dict):
        """
        Добавить новый фильм в БД
        :param data: dict с данными о фильме
        """
        self.dao.create(data)

    def update(self, data: dict):
        """
        Обновляет данные о фильме в БД
        :param data: dict с данными о фильме
        """
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

    def update_partial(self, data: dict):
        """
        Изменяет некоторые данные о фильме в БД
        :param data: dict с данными о фильме
        """
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

    def delete(self, id_: int):
        """
        Удаляет фильм из БД
        :param id_: id фильма
        :return:
        """
        self.dao.delete(id_)
