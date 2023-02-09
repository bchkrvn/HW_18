from dao.models.models import Director


class DirectorDAO:
    """
    Класс для взаимодействия с БД
    """
    def __init__(self, session):
        self.session = session

    def get_all(self) -> list[Director]:
        """
        Запросить всех режиссеров из БД
        :return: list[Director]
        """
        return self.session.query(Director).all()

    def get_one(self, id_: int) -> Director:
        """
        Запросить одного режиссера из БД
        :param id_: id режиссера
        :return: Director
        """
        return self.session.query(Director).get(id_)

    def create(self, data: dict):
        """
        Создать нового режиссера в БД
        :param data: данные о режиссере
        """
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()

    def update(self, director: Director):
        """
        Обновить данные о режиссере в БД
        :param director: Director
        """
        self.session.add(director)
        self.session.commit()

    def delete(self, id_: int):
        """
        Удалить данные о режиссере из БД
        :param id_: id режиссера
        """
        director = self.get_one(id_)
        self.session.delete(director)
        self.session.commit()
