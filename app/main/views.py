from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import main
from .. import db
from ..models import Issue

@main.route('/')
def welcome():
    return render_template('welcome.html', title="Welcome")

@main.route('/dashboard')
@login_required
def dashboard():
    issue_count = Issue.query.filter(Issue.user_id == current_user.id).count()
    resolved_issues = (Issue.query
        .filter(Issue.user_id == current_user.id)
        .filter(Issue.is_resolved == True)
        ).count()
    issues_in_progress = (Issue.query
        .filter(Issue.user_id == current_user.id)
        .filter(Issue.is_assigned == True)
        ).count()

    counts = dict(issue_count=issue_count, resolved_issues=resolved_issues, issues_in_progress=issues_in_progress)
    return render_template('dashboard.html', counts=counts, title="Dashboard")





