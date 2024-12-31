from flask import Blueprint
from src.infra.database import query
from flask import jsonify

api = Blueprint("api", __name__)


@api.route("/status", methods=["GET"])
def status():
    database_version_result = query("SELECT version();")[0][0]
    database_max_connections_result = query(
        "SHOW variables LIKE 'max_connections';")[0][1]
    database_open_connections_result = query(
        "SHOW STATUS WHERE variable_name = 'threads_connected';")[0][1]
    return jsonify({
        "database_version_result": database_version_result,
        "database_max_connections_result": int(database_max_connections_result),
        "database_open_connections_result": int(database_open_connections_result)
    })
