from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from chico_delivery.ext.auth.models import User
from chico_delivery.ext.db import db
from flask import flash


def format_user(self, request, user, *args):
    return user.email.split("@")[0]


class UserAdmin(ModelView):
    """INTERFACE ADMIN DE USER"""
    column_formatters = {"email" : format_user}

    column_list = ['email', 'admin']
    column_searchable_list = ["email"]
    column_filters = ["email", "admin"]

    can_edit = True
    can_create = True
    can_delete = True


    @action(
        'taggle_admin',
        'taggle admin status',
        'tem certeza, macho ?'
    )
    def tiggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f" {len(users)} Usuários alterados com sucesso")