from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, id_):
        return self.dao.get_one(id_)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        id_ = data.get('id')
        director = self.dao.get_one(id_)
        director.name = data.get('name')
        self.dao.update(director)

    def update_partial(self, data):
        id_ = data.get('id')
        director = self.dao.get_one(id_)
        if 'name' in data:
            director.name = data.get('name')
        self.dao.update(director)

    def delete(self, id_):
        self.dao.delete(id_)
