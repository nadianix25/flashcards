from app.models import Card


def test_card(app, new_card):
    """
    When "/card" is acessed with GET method and All param
    Check the status_code 200
    """
    with app.test_client() as test_client:
        response = test_client.get("card/All")
        assert response.status_code == 200

    """
    When "/card" is acessed with GET method and <card_name> param
    Check the status_code 200
    """
    with app.test_client() as test_client:
        response = test_client.get("card/group/Test Group")
        assert response.status_code == 200

    """
    When "/card" is acessed with DELETE method and ID param
    Check if the card is deleted
    """
    with app.test_client() as test_client:
        response = test_client.get("card/1")
        assert response.status_code == 200

    """
    When "/card" is acessed with GET method and NO params
    Check the status_code 405
    """
    with app.test_client() as test_client:
        response = test_client.get("card/")
        assert response.status_code == 405
