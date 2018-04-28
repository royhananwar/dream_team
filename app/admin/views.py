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

@admin.route('/department/add', methods=['POST', 'GET'])
@login_required
def add_department():
    '''
    Add new department
    '''
    check_admin()
    add_department = True

    form = DepartmenForm()
    if request.method == 'POST' and form.validate_on_submit():
        department = Department(
            name=form.name.data,
            description=form.description.data
        )
        try:
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            flash('can\'t add new department, Department name already exists!')
        finally:
            return redirect(url_for('admin.list_departments'))

    return render_template(
        'admin/departments/add.html',
        action='Add',
        add_department=add_department,
        form=form,
        title='Add Department'
        )
