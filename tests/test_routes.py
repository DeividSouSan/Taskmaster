import requests


def test_status_return_200():
    response = requests.get("http://localhost:3000/status")

    assert response.status_code == 200
    assert response.json()["database_version_result"] == "9.1.0"
    assert response.json()["database_max_connections_result"] == 151
