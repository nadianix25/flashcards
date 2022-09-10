# flashcards
Flashcards web app with flask

Flashcards are card notes used to pratice memory. They contain concepts and information. Basically you pick a card, look at the concept and try to retrieve the information withtout looking. 

This application mimics that process! Its a CRUD for cards and groups of cards that then will let you in a vizualization mode of the cards for pratice.
Its a web application in python using flask, it has been developed as an exercise to implement good practice (so its a Work In Progress).
###### I'm just going to highlight a few things I used

      * SQL ORM - SQLalchemy
      * Testing - Pytest
      * To dump objects from database - marshmallow-sqlalchemy

## Installation
To install dependencies please run the following command:
```
  pip install -r requirements.txt
```
**Set up your database and make sure it is accepting connections, you will need to change the reference on the config.py file (to match your database)**

To run server:
```
  flask --app app --debug run 
```
or just 

```
flask --app app run
```

## Testing
The tests runs on a sqlite database configured when the test config is used.
To run tests:
```
python -m pytest
```

Specific folder:
```
python -m pytest test/unit
```

Last failed test
```
python -m pytest --last-failed
```
