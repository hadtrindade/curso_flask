from flask_migrate import Migrate
from chico_delivery.ext.db import db

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
