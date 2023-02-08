from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, id_):
        return self.dao.get_one(id_)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        id_ = data.get('id')
        genre = self.dao.get_one(id_)
        genre.name = data.get('name')
        self.dao.update(genre)

    def update_partial(self, data):
        id_ = data.get('id')
        genre = self.dao.get_one(id_)
        if 'name' in data:
            genre.name = data.get('name')
        self.dao.update(genre)

    def delete(self, id_):
        self.dao.delete(id_)
