# flashcards
Flashcards web app with flask

to install dependencies please run the following command:
  pip install -r requirements.txt

To run server:
  flask --app app --debug run

To initialized database please run:

  flask --app app init db

To create DATABASE
first make sure we have all the configurations needed
>>> from app.models import db, Card, Group
>>> db.create_all()
>>> exit()


To run python black:
   python -m black .


To run tests:
python -m pytest

specifics:
python -m pytest test/unit


last failed
python -m pytest --last-failed
