import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, json
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import db, Card

bp = Blueprint('card', __name__, url_prefix='/card')


@bp.route('/', methods=('POST', 'PUT', 'DELETE'))
def register():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        hint = request.form['hint']
        error = None

        if not title:
            error = 'Title is required'
        elif not content:
            error = 'Content is required'

        flash(error)  # what is this?

        c = Card(title=title, content=content, hint=hint)
        db.session.add(c)
        db.session.commit()

    return redirect(url_for('home.home'))


@bp.route('/', methods=(['GET']))
def users():

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
