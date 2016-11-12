from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.config.from_object(config[config_name])
    app.config['SECRET_KEY'] = 'you-will-never-guess'
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/departments')

    from .issues import issues as issues_blueprint
    app.register_blueprint(issues_blueprint, url_prefix='/issues')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html', title="404 Error"), 404

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('403.html', title="403 Error"), 403

    return app
