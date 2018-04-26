from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DepartmenForm(FlaskForm):
    '''
    Form for edit or add department
    '''

    name = StringField('Departmen Name', validators=[DataRequired()])
    description = StringField('Departmen Description', validators=[DataRequired()])
    submit = SubmitField('Submit')