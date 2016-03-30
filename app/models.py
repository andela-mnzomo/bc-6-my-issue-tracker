from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db
from . import login_manager

class Role(db.Model):
    ''' Creates user role '''

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class User(UserMixin, db.Model):
    ''' Creates user '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role',
                           backref=db.backref('users', lazy='dynamic'))


    @property
    def password(self):
        '''prevents access to password
        property
        '''
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        '''Sets password to a hashed password
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        '''Checks if password matches
        '''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Comment(db.Model):
    ''' Creates comment '''

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User',
                           backref=db.backref('comments', lazy='dynamic'))


class Department(db.Model):
    ''' Creates department '''
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    dept_head = db.Column(db.Integer)



class Issue(db.Model):
    ''' Creates issue '''

    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(70))
    description = db.Column(db.Text)
    priority = db.Column(db.String(10))
    closed = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User',
                           backref=db.backref('issues', lazy='dynamic'))

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    department = db.relationship('Department',
                                 backref=db.backref('departments',
                                                    lazy='dynamic'))