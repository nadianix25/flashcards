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
    groups = Group.query.all()
    return render_template("slide/slideshow.html")
