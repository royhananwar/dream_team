from flask import abort, render_template
from flask_login import current_user, login_required

from . import home


@home.route('/')
def index():
    '''
    Render the homepage template to / route
    '''

    return render_template('home/index.html', title='Welcome to The Jungle')


@home.route('/dashboard')
@login_required
def dashboard():
    '''
    Render the dashboard to /dashboard route
    '''
    return render_template('home/dashboard.html', title='Dashboard')


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Prevennt if normal user access admin page
    if not current_user.is_admin:
        abort(403)
    
    return render_template('home/admin_dashboard.html', title='Admin Dashboard')