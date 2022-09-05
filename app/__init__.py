import os

from flask import Flask
from . import db, card, home, group


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
#    app.config.from_mapping(
#        SECRET_KEY="dev",
#        DATABASE=os.path.join(app.instance_path, "fcards.sqlite"),
#    )

    db.init_app(app)

    app.register_blueprint(card.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(group.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return "Hello this is the home page"

    return app
