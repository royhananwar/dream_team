from flask import Blueprint

app = Blueprint('home', __name__)

from . import views