from dao.models.models import Genre


class GenreDAO:
    """
    Класс для взаимодействия с БД
    """
    def __init__(self, session):
        self.session = session

    def get_all(self) -> list[Genre]:
        """
        Запрос всех жанров из БД
        :return: list[Genre]
        """
        return self.session.query(Genre).all()

    def get_one(self, id_: int) -> Genre:
        """
        Запрос одного жанра из БД
        :param id_: id жанра
        """
        return self.session.query(Genre).get(id_)

    def create(self, data: dict):
        """
        Создание нового жанра в БД
        :param data: данные о жанре
        """
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()

    def update(self, genre: Genre):
        """
        Обновление данных о жанре в БД
        :param genre: Genre
        """
        self.session.add(genre)
        self.session.commit()

    def delete(self, id_: int):
        """
        Удаление жанра из БД
        :param id_: id жанра
        """
        genre = self.get_one(id_)
        self.session.delete(genre)
        self.session.commit()
