
def test_home_page(app):
    """
    describe this please
    this will not work because of the database
    """
    with app.test_client() as test_client:
        response = test_client.get('home')
        assert response.status_code == 308
