from flask import Blueprint

app = Blueprint('auth', __name__)

from . import views