from flask_restx import Resource, Namespace
from flask import request

from container import genre_service
from dao.models.models import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    def post(self):
        new_genre = request.json
        genre_service.create(new_genre)
        return '', 201


@genre_ns.route('/<int:id_>')
class GenreViews(Resource):
    def get(self, id_):
        genre = genre_service.get_one(id_)
        return genre_schema.dump(genre), 200

    def put(self, id_):
        update_genre = request.json
        update_genre['id'] = id_
        genre_service.update(update_genre)

        return '', 204

    def patch(self, id_):
        patch_genre = request.json
        patch_genre['id'] = id_
        genre_service.update_partial(patch_genre)

        return '', 204

    def delete(self, id_):
        genre_service.delete(id_)
        return '', 204
