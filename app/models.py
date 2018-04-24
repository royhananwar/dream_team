from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Employee(UserMixin, db.Model):
    '''
    Employee Tabel
    '''

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    departmen_id = db.Column(db.Integer, db.ForeignKey('departmens.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        '''
        Prevent to access password
        '''
        raise AttributeError('Password is not Readable!')

    @password.setter
    def password(self):
        '''
        set password to a hashed password
        '''
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self):
        '''
        Check password if match with hash password
        '''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}'.format(self.username)
