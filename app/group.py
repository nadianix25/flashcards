import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('group', __name__, url_prefix='/group')


@bp.route('/', methods=('GET', 'POST', 'PUT', 'DELETE'))
def register():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        db = get_db()
        error = None

        if not title:
            error = 'Title is required'
        elif not description:
            error = 'Description is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO groups (title, description) VALUES (?, ?)",
                    (title, description),
                )
                db.commit()
            except db.IntegrityError:
                error = f"title {title} is already exists."
            else:
                return "U saved a group"

        flash(error)  # what is this?

    return render_template('card/form.html')
