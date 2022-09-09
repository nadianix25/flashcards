from app.models import Card, Group


def test_new_card():
    """
    describe this please
    """
    card = Card(title='Some title', content='Sql is amazing', hint="Some hint")
    assert card.title == 'Some title'
    assert card.content == 'Sql is amazing'
    assert card.hint == 'Some hint'
