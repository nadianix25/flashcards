"""This is the pratice Blueprint module.

This module perform specefic actions to the pratice endpoint
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
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import Card, Group


bp = Blueprint("pratice", __name__, url_prefix="/pratice")


@bp.route("/<group>", methods=(["GET"]))
def prepare_group(group):
    if group == "All":
        group = {'title': "All cards", 'description': "Group of all the cards"}
        cards = Card.query.all()
    else:
        group = Group.query.filter_by(title=group).first()
        cards = Card.query.join(Card.groups).filter_by(id=group.id).all()

    return render_template("slide/slideshow.html", cards=cards, group=group)
