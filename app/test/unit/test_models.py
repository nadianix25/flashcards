from app.models import db, Card, Group


def test_new_card(new_card):
    """
    describe this please
    """
    assert new_card.title == "Some title"
    assert new_card.content == "Sql is amazing"
    assert new_card.hint == "Some hint"


def test_new_group(new_group):
    """
    describe this please
    """
    assert new_group.title == "Test Group"
    assert new_group.description == "Just a test group"
