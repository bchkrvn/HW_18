from dao.director import DirectorDAO


class DirectorService:
    """
    Класс для связи view и dao
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self) -> list:
        """
        Получить всех режиссеров из БД
        :return: list
        """
        return self.dao.get_all()

    def get_one(self, id_: int):
        """
        Получить режиссера по его id из БД
        :param id_: id режиссера
        """
        return self.dao.get_one(id_)

    def create(self, data: dict):
        """
        Создать нового режиссера в БД
        :param data: данные о режиссере
        :return:
        """
        self.dao.create(data)

    def update(self, data):
        """
        Обновить данные о режиссере в БД
        :param data: данные о режиссере
        """
        id_ = data.get('id')
        director = self.dao.get_one(id_)
        director.name = data.get('name')
        self.dao.update(director)

    def update_partial(self, data):
        """
        Изменить некоторые данные о режиссере в БД
        :param data: данные о режиссере
        """
        id_ = data.get('id')
        director = self.dao.get_one(id_)
        if 'name' in data:
            director.name = data.get('name')
        self.dao.update(director)

    def delete(self, id_):
        """
        Удалить данные о режиссере из БД
        :param id_: id режиссера
        """
        self.dao.delete(id_)
