from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, StringField, PasswordField, BooleanField, ValidationError, validators

from ..models import db, User

class SignupForm(Form):
  ''' Form for users to create new account '''
  fullname = TextField("Full Name",  [validators.Required("Please enter your  name.")])
  username = TextField("Username",  [validators.Required("Please select a username."), 
                                      validators.Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                      'Usernames must have only letters, '
                                      'numbers, dots or underscores')])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
  confirm = PasswordField('Confirm Password')
  submit = SubmitField("Create account")
 
  def validate_email(self, field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError('Email already registered.')

  def validate_username(self, field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError('Username already in use.')

class LoginForm(Form):
  ''' Form for users to login '''
  email = StringField('Email', [validators.Required(), validators.Length(1, 64), validators.Email()])
  password = PasswordField('Enter Password', [
        validators.Required()
    ])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField("Login")