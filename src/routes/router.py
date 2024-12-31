from flask import Blueprint

api = Blueprint("api", __name__)


@api.route("/status", methods=["GET"])
def status():
    return "<h1>Olá</h1>"
