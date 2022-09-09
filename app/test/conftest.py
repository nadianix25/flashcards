from app import create_app
from app.models import db, Card, Group
import pytest


@pytest.fixture(scope="session")
def new_card():
    card = Card(title='Some title', content='Sql is amazing', hint="Some hint")
    return card


@pytest.fixture(scope="session")
def app():
    return give_me_app()


def give_me_app():
    app = create_app('flask_test.cfg')
    app.app_context().push()
    db.drop_all(app=app)  # clean database
    db.create_all(app=app)  # create database
    seed_database()
    return app


def seed_database():
    c1 = Card(title='a card', content='what', hint="no hints")
    c2 = Card(title='b card', content='when', hint="nothing to add")
    c3 = Card(title='c card', content='who', hint="no words")

    db.session.add_all([c1, c2, c3])
    db.session.commit()

    return
