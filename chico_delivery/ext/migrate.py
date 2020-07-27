from flask_migrate import Migrate
from chico_delivery.ext.db import db
from chico_delivery.ext.db import models #noqa

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
