def test_ping(test_app):
    """
    Checks the API Server Status
    """
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}


def test_list_currencies(test_app):
    """
    Tests Getting the list of supported currencies
    """
    response = test_app.get("/currency/list")
    assert response.status_code == 200
