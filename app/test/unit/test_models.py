from app.models import db, Card, Group


def test_new_card(new_card):
    """
    describe this please
    """
    card = new_card
    db.session.add(card)
    db.session.commit()
    list = Card.query.all()
    assert len(list) == 1
    assert new_card.title == 'Some title'
    assert new_card.content == 'Sql is amazing'
    assert new_card.hint == 'Some hint'
