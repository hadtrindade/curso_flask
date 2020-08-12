from flask import Flask
from chico_delivery.ext import config


def create_app():
    """
    Factory principal.

    Returns:
        obg: app flask
    """

    app = Flask(__name__)
    config.init_app(app)
    return app
