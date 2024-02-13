from flask import Blueprint, redirect, request, render_template, url_for
from src.forms.register import RegisterForm
from src.use_case.user.register_user_use_case import RegisterUserUseCase
from src.repositories import user_repository


bp = Blueprint("website", __name__)


@bp.route("/")
def index():
    return render_template("index.html", title="Taskmaster - Index")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    error = None
    if request.method == "POST":
        if form.validate_on_submit():

            useCase = RegisterUserUseCase(form)
            result = useCase.execute()

            if result == True:
                redirect(url_for('website.register'))    
            error = useCase.error

    return render_template("register.html", form=form, error=error, title="Taskmaster - Cadastro")
