from flask import render_template, flash, redirect, request, url_for, abort
from flask.ext.login import login_user, logout_user, login_required, current_user
from datetime import datetime
from . import issues
from forms import IssueForm
from ..models import Issue, User
from .. import db

@issues.route('/raise', methods=['GET', 'POST'])
@login_required
def raise_issue():
	form = IssueForm()
	if form.validate_on_submit():
		issue = Issue(subject=form.subject.data,
                    description=form.description.data,
                    priority=form.priority.data,
                    department_id=form.department.data,
                    user=current_user._get_current_object())
		db.session.add(issue)
		db.session.commit()
		flash('Thanks! We have recorded your issue.')
	return render_template('issues/raise.html', form = form, title = "Raise Issue")

@issues.route('/view')
@login_required
def view():
	issues = (Issue.query
		.filter(Issue.user_id == current_user.id)
		.order_by(Issue.raised_at.desc())
		).all()
	return render_template('issues/view.html', issues=issues, title="My Issues")

@issues.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
	issue = Issue.query.get_or_404(id)
	if current_user.id != issue.user_id:
		abort(403)
	form = IssueForm(obj=issue)
	if form.validate_on_submit():
		issue.subject = form.subject.data
		issue.description = form.description.data
		issue.priority = form.priority.data
		issue.department_id = form.department.data
		issue.user=current_user._get_current_object()
		db.session.add(issue)
		db.session.commit()
		flash('Your issue has been updated.')
	form.description.data = issue.description
	form.subject.data = issue.subject
	return render_template('issues/edit.html', form=form, title="Edit Issue")

@issues.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
	issue = Issue.query.get_or_404(id)
	if current_user.id != issue.user_id:
		abort(403)
	db.session.delete(issue)
	return render_template('issues/delete.html', issue=issue, title="Delete Issue")

@issues.route('/deleting/<int:id>', methods=['GET', 'POST'])
@login_required
def deleting(id):
	issue = Issue.query.get_or_404(id)
	db.session.delete(issue)
	db.session.commit()
	return redirect(url_for('issues.view'))
	return render_template('issues/delete.html', issue=issue)

@issues.route('/admin/view')
@login_required
def admin_view():
	issues = Issue.query.order_by(Issue.raised_at.desc()).all()
	return render_template('issues/view-admin.html', issues=issues, title="Issues Raised")

@issues.route('/admin/resolve/<int:id>', methods=['GET', 'POST'])
@login_required
def resolve(id):
	issue = Issue.query.get_or_404(id)
	if current_user.is_admin == False:
		abort(403)
	return render_template('issues/resolve.html', issue=issue, title="Resolve Issue")

@issues.route('/admin/resolving/<int:id>', methods=['GET', 'POST'])
@login_required
def resolving(id):
	issue = Issue.query.get_or_404(id)
	issue.is_resolved=True
	db.session.add(issue)
	db.session.commit()
	return redirect(url_for('issues.admin_view'))
	return render_template('issues/resolve.html', issue=issue)

@issues.route('/admin/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign(id):
	issue = Issue.query.get_or_404(id)
	users = User.query.all()
	return render_template('issues/assign.html', issue=issue, users=users, title="Assign Issue")

@issues.route('/admin/assigning/<int:id>', methods=['GET', 'POST'])
@login_required
def assigning(id):
	issue = Issue.query.get_or_404(id)
	issue.is_assigned=True
	db.session.add(issue)
	db.session.commit()
	return redirect(url_for('issues.admin_view'))
	return render_template('issues/assign.html', issue=issue)


	