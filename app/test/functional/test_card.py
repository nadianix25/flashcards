def test_card(app):
    """
    describe this please
    this will not work because of the database
    """
    with app.test_client() as test_client:
        response = test_client.get('card/All')
        assert response.status_code == 200
