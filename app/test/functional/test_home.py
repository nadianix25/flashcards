from app import create_app


def test_home_page():
    """
    describe this please
    this will not work because of the database
    """

    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get('home')
        assert response.status_code == 308
