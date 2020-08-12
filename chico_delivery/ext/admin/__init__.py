from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from chico_delivery.ext.db import db
from chico_delivery.ext.db.models import Category


admin = Admin()


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Chico_Delivery")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap3")
    admin.init_app(app)
    admin.add_view(ModelView(Category, db.session))
