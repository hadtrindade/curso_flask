from flask import request, render_template, request, redirect
from flask import Blueprint
from chico_delivery.ext.auth.form import UserForm
from chico_delivery.ext.auth.controller import (
    create_user,
    save_user_photo,
)


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")


@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        create_user(
            email=form.email.data,
            password=form.password.data
        )
        photo = request.files.get("foto")
        if photo:
            save_user_photo(
                photo,
                photo.filename,
                )
        #forçar login
        return redirect("/")
    return render_template("userform.html", form=form)