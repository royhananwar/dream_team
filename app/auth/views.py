from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import RegistrationForm, LoginForm
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Handle for register new Account
    '''
    
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        employee = Employee(
            email=form.email.data,
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )

        # add new employee to DB
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered! You may now login.')
        
        # redirect to login page
        return redirect(url_for('auth.login'))

    # render template and load registration form
    return render_template('auth/register.html', form=form, title='Register')

