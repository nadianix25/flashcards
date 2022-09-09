import os

basedir = os.path.abspath(os.path.dirname("instance"))


class Config:
    SECRET_KEY = "dev"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5455"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Test:
    SECRET_KEY = "dev"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(basedir, "fcards.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
