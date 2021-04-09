from config import config
from flask import Flask

from project.apis import api
from project.extensions import db, migrate


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)

    return app


def register_extensions(app):
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
