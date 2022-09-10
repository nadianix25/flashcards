# flashcards
Flashcards web app with flask

Flashcards are card notes used to pratice memory. They contain concenpts and information. Basically you pick a card, look at the concept i try to retrieve the information withtout looking. 

This application mimics that process! Its a CRUD for cards and groups of cards that then will let you in a vizualization mode of the cards for pratice.

to install dependencies please run the following command:
```
  pip install -r requirements.txt
```

To run server:
```
  flask --app app --debug run
```  

To create DATABASE
first make sure we have all the configurations needed
```
from app.models import db, Card, Group
db.create_all()
exit()
```

To run python black:
```
   python -m black 
```

To run tests:
```
python -m pytest
```

specifics:
```
python -m pytest test/unit
```

last failed
```
python -m pytest --last-failed
```
