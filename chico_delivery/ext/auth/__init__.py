from chico_delivery.ext.auth import models #noqa
from chico_delivery.ext.auth.commands import add_user, list_users
from chico_delivery.ext.auth.admin import UserAdmin
from chico_delivery.ext.admin import admin
from chico_delivery.ext.db import db
from chico_delivery.ext.auth.models import User


def init_app(app):
    """TODO aqui vai o flask simple login + JWT."""
    app.cli.command()(add_user)
    app.cli.command()(list_users)
    admin.add_view(UserAdmin(User, db.session))