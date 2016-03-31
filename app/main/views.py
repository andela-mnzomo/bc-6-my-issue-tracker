from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required
from . import main
from .. import db

@main.route('/')
def welcome():
    return render_template('welcome.html', title= "Welcome")

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title= "Dashboard")


