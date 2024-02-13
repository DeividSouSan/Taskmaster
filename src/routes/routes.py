from flask import Blueprint, request, render_template, url_for
from src.forms.register import RegisterForm
from src.use_case.user.register_user_use_case import RegisterUserUseCase


bp = Blueprint("website", __name__)


@bp.route("/")
def index():
    return render_template("index.html", title="Taskmaster - Index")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if request.method == "POST":
        if form.validate_on_submit():
            useCase = RegisterUserUseCase(form)
            useCase.execute()

    return render_template("register.html", form=form)
