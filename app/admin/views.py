from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required, current_user
from forms import DepartmentForm
from . import admin
from ..models import Department
from .. import db

@admin.route('/add', methods=['GET', 'POST'])
@login_required
def add():
	form = DepartmentForm()
	if form.validate_on_submit():
		department = Department(name=form.name.data,
                    user_id=form.dept_admin.data)
		db.session.add(department)
		db.session.commit()
		flash('You have successfully added a new department.')
		return redirect(url_for('admin.view'))
	return render_template('admin/add.html', form = form, title = "Add Department")

@admin.route('/view')
@login_required
def view():
	departments = Department.query.all()
	return render_template('admin/view.html', departments=departments, title="View Departments")

@admin.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
	department = Department.query.get_or_404(id)
	# if current_user.id != issue.user_id:
	# 	abort(403)
	form = DepartmentForm(obj=department)
	if form.validate_on_submit():
		department.name = form.name.data
		department.user_id = form.dept_admin.data
		db.session.add(department)
		db.session.commit()
		return redirect(url_for('admin.view'))
	form.name.data = department.name
	form.dept_admin.data = department.user_id
	return render_template('admin/edit.html', form=form, title="Edit Department")

@admin.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
	department = Department.query.get_or_404(id)
	if current_user.is_admin == False:
		abort(403)
	return render_template('admin/delete.html', department=department, title="Delete Department")

@admin.route('/deleting/<int:id>', methods=['GET', 'POST'])
@login_required
def deleting(id):
	department = Department.query.get_or_404(id)
	db.session.delete(department)
	db.session.commit()
	return redirect(url_for('admin.view'))
	return render_template('admin/delete.html', department=department)