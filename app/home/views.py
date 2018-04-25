from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
def index():
    '''
    Render the homepage template to / route
    '''

    return render_template('home/index.html', title='Welcome to The Jungle')