"""This is the home Blueprint module.

This module perform specefic actions to the group endpoint
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


bp = Blueprint("home", __name__, url_prefix="/home")


@bp.route("/", methods=(["GET"]))
def home():
    groups = Group.query.all()
    return render_template("home/dashboard.html", groups=groups)
