from flask import render_template, flash, redirect, request, url_for
from . import main
from .. import db

@main.route('/')
def home():
    return render_template('dashboard.html', title= "Dashboard")


@main.errorhandler(404)
def not_found(error):
    return render_template('404.html', title="404 Error"), 404


