import os
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from werkzeug.utils import secure_filename
from flask import current_app as app
from chico_delivery.ext.auth.models import User
from chico_delivery.ext.db import db


ALG = "pbkdf2:sha256"

def create_user(email: str, password: str, admin=False) -> User:
    user = User(
        email=email,
        passwd=generate_password_hash(password, ALG),
        admin=admin,
    )
    db.session.add(user)
    # TODO: tratar excessao de 
    db.session.commit()
    return user


def save_user_photo(filename, filestorage):
    os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename)
        
    )
    filestorage.save()