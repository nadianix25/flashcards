import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import card, home, group, models


# create and configure the app
def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object("app.config.Config")
        models.db.init_app(app)

    else:
        # load the test config if passed in
        app.config.from_object("app.config.Test")
        models.db.init_app(app)
        #models.db.create_all(app=app)

    app.register_blueprint(card.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(group.bp)

    return app
