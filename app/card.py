"""This is the card Blueprint module.

This module perform specefic actions to the card endpoint
it must be resgister in the app
"""

import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    json,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import db, Card, Group, CardSchema

bp = Blueprint("card", __name__, url_prefix="/card")


@bp.route("/", methods=(["POST"]))
def register():
    obJson = request.get_json()
    group = obJson.get('group')
    title = obJson.get('title')
    content = obJson.get('content')
    hint = obJson.get('hint')

    if len(group) > 0:
       c = Card(title=title, content=content, hint=hint)
       db.session.add(c)
       db.session.commit()
       g = Group.query.filter_by(title=group).first()
       c.groups.append(g)
       db.session.commit()

    return (
        json.dumps({"success": True}),
        200,
        {"ContentType": "application/json"},
    )


@bp.route("/group/<filter>", methods=(["GET"]))
def cards_in_group(filter):
    if len(filter) > 0:
        schema = CardSchema()
        data = []

        if filter == "All":
            cards = Card.query.all()
        else:
            group = Group.query.filter_by(title=filter).first()
            cards = Card.query.join(Card.groups).filter_by(id=group.id).all()

        for card in cards:
            data.append(schema.dump(card))
    else:
        pass

    return (
        json.dumps({"success": True, "data": data}),
        200,
        {"ContentType": "application/json"},
    )


@bp.route("/<id>", methods=(["GET"]))
def cards(id):

    card = Card.query.filter_by(id=id).first()
    schema = CardSchema()
    data = schema.dump(card)

    return (
        json.dumps({"success": True, "data": data}),
        200,
        {"ContentType": "application/json"},
    )


@bp.route("/<id>", methods=(["DELETE"]))
def delete(id):

    card = Card.query.filter_by(id=id).first()
    db.session.delete(card)
    db.session.commit()

    return (
        json.dumps({"success": True}),
        200,
        {"ContentType": "application/json"},
    )


@bp.route("/<id>", methods=(["PATCH"]))
def update(id):
    obJson = request.get_json()
    id = obJson.get('id')
    title = obJson.get('title')
    content = obJson.get('content')
    hint = obJson.get('hint')

    card = Card.query.filter_by(id=id).first()
    card.title = title
    card.content = content
    card.hint = hint
    db.session.commit()
    return (
        json.dumps({"success": True}),
        200,
        {"ContentType": "application/json"},
    )
