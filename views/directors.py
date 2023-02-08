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
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    def post(self):
        new_director = request.json
        director_service.create(new_director)
        return '', 201


@director_ns.route('/<int:id_>')
class DirectorViews(Resource):
    def get(self, id_):
        director = director_service.get_one(id_)
        return director_schema.dump(director), 200

    def put(self, id_):
        update_director = request.json
        update_director['id'] = id_
        director_service.update(update_director)

        return '', 204

    def patch(self, id_):
        patch_director = request.json
        patch_director['id'] = id_
        director_service.update_partial(patch_director)

        return '', 204

    def delete(self, id_):
        director_service.delete(id_)
        return '', 204
