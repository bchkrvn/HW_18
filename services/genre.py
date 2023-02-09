from dao.genre import GenreDAO


class GenreService:
    """
    Класс для связи view и dao
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self) -> list:
        """
        Получить все жанры из БД
        :return: list
        """
        return self.dao.get_all()

    def get_one(self, id_: int):
        """
        Получить жанр по его id из БД
        :param id_: id жанра
        :return:
        """
        return self.dao.get_one(id_)

    def create(self, data: dict):
        """
        Создать новый жанр в БД
        :param data: dict с данными о жанре
        """
        self.dao.create(data)

    def update(self, data: dict):
        """
        Обновить данные о жанре в БД
        :param data: dict с данными о жанре
        """
        id_ = data.get('id')
        genre = self.dao.get_one(id_)
        genre.name = data.get('name')
        self.dao.update(genre)

    def update_partial(self, data: dict):
        """
        Частично изменить данные о жанре в БД
        :param data: dict с данными о жанре
        """
        id_ = data.get('id')
        genre = self.dao.get_one(id_)
        if 'name' in data:
            genre.name = data.get('name')
        self.dao.update(genre)

    def delete(self, id_: int):
        """
        Удалить жанр из БД
        :param id_: id жанра
        :return:
        """
        self.dao.delete(id_)
