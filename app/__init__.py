import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import card, home, group, models


# create and configure the app
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
           SECRET_KEY="dev"
        )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5455'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #        DATABASE=os.path.join(app.instance_path, "fcards.sqlite"),

    models.db.init_app(app)

    app.register_blueprint(card.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(group.bp)
    return app
