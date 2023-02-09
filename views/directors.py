from flask_restx import Resource, Namespace
from flask import request

from container import director_service
from dao.models.models import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        """
        Позволяет получить всех режиссеров
        """
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    def post(self):
        """
        Позволяет добавить нового режиссера
        """
        new_director = request.json
        director_service.create(new_director)
        return '', 201


@director_ns.route('/<int:id_>')
class DirectorViews(Resource):
    def get(self, id_):
        """
        Позволяет получить режиссера по его id
        :param id_: id режиссера
        """
        director = director_service.get_one(id_)
        if director:
            return director_schema.dump(director), 200
        else:
            return '', 404

    def put(self, id_):
        """
        Позволяет изменить режиссера
        :param id_: id режиссера
        """
        update_director = request.json
        update_director['id'] = id_
        director_service.update(update_director)

        return '', 204

    def patch(self, id_):
        """
        Позволяет обновить режиссера
        :param id_: id режиссера
        """
        patch_director = request.json
        patch_director['id'] = id_
        director_service.update_partial(patch_director)

        return '', 204

    def delete(self, id_):
        """
        Позволяет удалить режиссера
        :param id_: id режиссера
        """
        director_service.delete(id_)
        return '', 204
