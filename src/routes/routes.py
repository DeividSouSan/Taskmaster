from datetime import datetime
from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from src.models.user import User
from src.server import server


bp = Blueprint("tasks", __name__)


@bp.route("/add", methods=["POST"])
def index():
    user = User(
        username="Deivisousn",
        password_hash="1234",
        fullname="Deivid Souza Santana",
        email="deividsantana2013@gmail.com",
        registration=datetime.now()
    )

    server.db.session.add(user)
    server.db.session.commit()
    server.db.session.close()

    return jsonify({user}), 200
