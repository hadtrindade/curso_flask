from flask import Flask
from chico_delivery.ext import site
from chico_delivery.ext import toolbar
from chico_delivery.ext import config
from chico_delivery.ext import db
from chico_delivery.ext import migrate
from chico_delivery.ext import cli


def create_app():
    """
    Factory principal.

    Returns:
        obg: app flask
    """

    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)

    return app