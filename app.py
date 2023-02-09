from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app_config = Config()
app = create_app(app_config)

if __name__ == '__main__':
    app.run()
