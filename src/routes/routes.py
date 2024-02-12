from datetime import datetime
from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import text
from sqlalchemy.orm import Session
from src.forms.register import RegisterForm
from src.server.server import engine

from src.models.user import User
from src.use_case.user.register_user_use_case import RegisterUserUseCase


bp = Blueprint("tasks", __name__, template_folder="../templates")

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if request.method == "POST":
        if form.validate_on_submit():
            useCase = RegisterUserUseCase(form)
            useCase.execute()

    return render_template("sign_up.html", form=form)
