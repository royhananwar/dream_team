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
        form=form,
        title='Add Department'
        )

@admin.route('/department/edit/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_department(id):
    '''
    Edit existing department
    '''
    check_admin()

    department = Department.query.get_or_404(id)
    form = DepartmenForm(obj=department)

    if request.method == 'POST' and form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data

        db.session.commit()

        flash('You have successfuly update the Department')

        return redirect(url_for('admin.list_departments'))
    
    return render_template(
        'admin/departments/edit.html',
        form=form,
        title='Edit Department',
        department=department,
        )
