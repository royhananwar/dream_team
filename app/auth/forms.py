from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee


class RegistrationForm(FlaskForm):
    '''
    Form for create new account
    '''

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        employee = Employee.query.filter_by(email=field.data).first()
        if employee:
            return ValidationError('Email is already in use.')

    def validate_username(self, field):
        employee = Employee.query.filter_by(username=field.data).first()
        if employee:
            return ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    '''
    Form for users to Login
    '''

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')