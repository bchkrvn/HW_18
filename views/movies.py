from flask_restx import Resource, Namespace
from flask import request
from container import movie_service
from dao.models.models import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Позволяет получить список всех фильмов
        или фильмов определенного года, режиссера, жанра
        """
        year = request.values.get('year')
        genre_id = request.values.get('genre_id')
        director_id = request.values.get('director_id')
        all_movies = movie_service.get_all_filter(year, genre_id, director_id)

        return movies_schema.dump(all_movies), 200

    def post(self):
        """
        Позволяет добавить новый фильм в БД
        """
        new_movie = request.json
        movie_service.create(new_movie)

        return '', 201


@movie_ns.route('/<int:id_>')
class MovieView(Resource):
    def get(self, id_):
        """
        Позволяет получить фильм по его id
        :param id_: id фильма
        """
        movie = movie_service.get_one(id_)
        if not movie:
            return '', 404

        return movie_schema.dump(movie), 200

    def put(self, id_):
        """
        Позволяет полностью изменить информацию о существующем фильме
        :param id_: id фильма
        """
        update_movie = request.json
        update_movie['id'] = id_
        movie_service.update(update_movie)

        return '', 204

    def patch(self, id_):
        """
        Позволяет частично изменить информацию о существующем фильме
        :param id_: id фильма
        """
        patch_movie = request.json
        patch_movie['id'] = id_
        movie_service.update_partial(patch_movie)

        return '', 204

    def delete(self, id_):
        """
        Позволяет удалить фильма
        :param id_: id фильма
        """
        movie_service.delete(id_)
        return '', 204
