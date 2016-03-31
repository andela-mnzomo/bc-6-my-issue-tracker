from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SelectField, SubmitField, StringField, PasswordField, BooleanField, ValidationError, validators

from ..models import db, User, Issue, Department

class DepartmentForm(Form):
  ''' Form for admins to add department '''
  
  name = TextField("Department Name",  [validators.Required("Please enter a department name.")])
  dept_admin = SelectField('User',
                           [validators.Required(
                               message='Please select a department admin.')],
                           coerce=int)
  submit = SubmitField('Submit')

  def __init__(self, *args, **kwargs):
      super(DepartmentForm, self).__init__(*args, **kwargs)
      self.dept_admin.choices = [
          (user.id, user.fullname) for user in User.query.all()]