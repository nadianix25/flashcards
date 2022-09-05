import os
import psycopg2
import click
from flask import current_app, g


def get_db():
    conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user='postgres',
            password='postgres')

    return conn


def close_db(h):
    get_db().close()
    pass


def init_db():
    db = get_db()

    db.cursor().execute(open("app/schema.sql", "r").read())
    db.commit()
    db.close()


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
