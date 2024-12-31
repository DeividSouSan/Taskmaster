from flask import Blueprint
from src.infra.database import query
test = Blueprint("test", __name__)

@test.route("/test", methods=["GET"])
def teste():
    result = query("SELECT 1 + 1 AS SOMA")
    
    return F"<h1>{result}</h1>"