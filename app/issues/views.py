from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required
from . import issues
from forms import IssueForm
from .. import db

@issues.route('/raise', methods=['GET', 'POST'])
@login_required
def raise_issue():
	form = IssueForm()
	if form.validate_on_submit():
		issue = Issue(subject=form.subject.data,
                    description=form.description.data,
                    priority=form.priority.data,
                    department=form.department.data)
		db.session.add(issue)
		db.session.commit()
		flash('Thanks! We have recorded your issue.')
	return render_template('issues/raise.html', form = form, title = "Raise Issue")

@issues.route('/view')
@login_required
def view():
    return render_template('issues/view.html', title = "My Issues")