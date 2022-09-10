def test_home_page(app):
    """
    When "/home" is acessed
    Check the status_code 308
    """
    with app.test_client() as test_client:
        response = test_client.get("home")
        assert response.status_code == 308
