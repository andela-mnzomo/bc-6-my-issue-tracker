from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, StringField, PasswordField, BooleanField, validators

from ..models import db, User

class SignupForm(Form):
  ''' Form for users to create new account '''
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  username = TextField("Username",  [validators.Required("Please select a username.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
  confirm = PasswordField('Confirm Password')
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken.")
      return False
    else:
      return True

class LoginForm(Form):
  ''' Form for users to login '''
  email = StringField('Email', [validators.Required(), validators.Length(1, 64), validators.Email()])
  password = PasswordField('Enter Password', [
        validators.Required()
    ])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField("Login")