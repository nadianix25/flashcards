import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/home')

def get_cards():
    return get_db().execute('SELECT * FROM card').fetchall()

@bp.route('/', methods=(['GET']))
def home():
    cards = get_cards()
    return render_template('home/dashboard.html', cards=cards)
