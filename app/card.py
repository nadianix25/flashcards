import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('card', __name__, url_prefix='/card')


@bp.route('/', methods=('GET', 'POST', 'PUT', 'DELETE'))
def register():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        hint = request.form['hint']
        db = get_db()
        error = None

        if not title:
            error = 'Title is required'
        elif not content:
            error = 'Content is required'

        if error is None:
            try:
                db.cursor().execute(
                    "INSERT INTO card (title, content, hint) VALUES (%s, %s, %s)",
                    (title, content, hint),
                )
                db.commit()
            except db.IntegrityError:
                error = f"title {title} is already exists."
            else:
                return "U saved a card"

        flash(error)  # what is this?

    return render_template('card/form.html')
