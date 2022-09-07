import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import db, Group
bp = Blueprint('group', __name__, url_prefix='/group')


@bp.route('/', methods=('GET', 'POST', 'PUT', 'DELETE'))
def register():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        error = None

        if not title:
            error = 'Title is required'
        elif not description:
            error = 'Description is required'

        flash(error)  # what is this?

        g = Group(title=title, description=description)
        db.session.add(g)
        db.session.commit()

    return redirect(url_for('home.home'))
