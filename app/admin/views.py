from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import admin
from ..models import Department
from .forms import  DepartmenForm
from .. import db


def check_admin():
    '''
    check if user is admin or normal user
    '''
    if not current_user.is_admin:
        abort(403)


@admin.route('/departments', methods=['POST', 'GET'])
@login_required
def list_departments():
    '''
    List from department
    '''
    check_admin()

    departments = Department.query.all()
    return render_template(
        'admin/departments/departments.html', 
        departments=departments, 
        title='Departments'
        )