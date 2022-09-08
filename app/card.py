import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, json
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import db, Card, Group, CardSchema

bp = Blueprint('card', __name__, url_prefix='/card')


@bp.route('/', methods=(['POST']))
def register():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        hint = request.form['hint']
        group = request.form['group']

        error = None

        if not title:
            error = 'Title is required'
        elif not content:
            error = 'Content is required'

        flash(error)  # what is this?

        if len(group) > 0:
            c = Card(title=title, content=content, hint=hint)
            db.session.add(c)
            db.session.commit()
            g = Group.query.filter_by(title=group).first()
            c.groups.append(g)
            db.session.commit()

    return redirect(url_for('home.home'))


@bp.route('/<filter>', methods=(['GET']))
def users(filter):
    #recieving jsong here
    print("hello")
    if len(filter) > 0:
        schema = CardSchema()
        group = Group.query.filter_by(title=filter).first()
        cards = Card.query.join(Card.groups).filter_by(id=group.id).all()
        data = []

        for card in cards:
            data.append(schema.dump(card))

    else:
        pass

    return json.dumps({'success': True, 'data': data}), 200, {'ContentType': 'application/json'}
