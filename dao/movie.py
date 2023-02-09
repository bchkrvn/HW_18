from dao.models.models import Movie


class MovieDAO:
    """
    Класс для взаимодействия с БД
    """
    def __init__(self, session):
        self.session = session

    def get_all(self) -> list:
        """
        Запрос всех фильмов из БД
        :return: list
        """
        return self.session.query(Movie).all()

    def get_one(self, id_: int) -> Movie:
        """
        Запрос одного фильма из БД
        :param id_: id фильма
        :return: Movie
        """
        return self.session.query(Movie).get(id_)

    def get_by_year(self, year: int) -> list:
        """
        Запрос фильмов из БД определенного года
        :param year: год выпуска
        :return: list
        """
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_by_director(self, d_id: int) -> list:
        """
        Запрос фильмов из БД определенного режиссера
        :param d_id: id режиссера
        :return: list
        """
        return self.session.query(Movie).filter(Movie.director_id == d_id).all()

    def get_by_genre(self, g_id: int) -> list:
        """
        Запрос фильмов из БД определенного жанра
        :param g_id: id жанра
        :return: list
        """
        return self.session.query(Movie).filter(Movie.genre_id == g_id).all()

    def create(self, data: dict):
        """
        Создание нового фильма в БД
        :param data: данные о фильме
        """
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie: Movie):
        """
        Обновление данные о фильме
        :param movie: Movie
        """
        self.session.add(movie)
        self.session.commit()

    def delete(self, id_: int):
        """
        Удаление фильма из БД
        :param id_: id фильма
        """
        movie = self.get_one(id_)
        self.session.delete(movie)
        self.session.commit()
