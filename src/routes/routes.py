from datetime import datetime
from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker


bp = Blueprint("tasks", __name__, template_folder="../templates")


@bp.route("/", methods=["GET"])
def index():
    print('oi')
    return render_template("index.html")
