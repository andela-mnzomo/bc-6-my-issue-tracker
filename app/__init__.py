from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

def create_app(config_name):
	# Define the WSGI application object
	app = Flask(__name__)

	# Configurations
	app.config.from_object('config')

	# Define the database object which is imported by modules and controllers
	db = SQLAlchemy(app)

	# HTTP error handling
	@app.errorhandler(404)
	def not_found(error):
	    return render_template('404.html'), 404

	# Import a module / component using its blueprint handler variable 
	from app.auth.views import auth as auth_module

	# Register blueprints
	app.register_blueprint(auth_module)

	# Build the database:
	# This will create the database file using SQLAlchemy
	db.create_all()
