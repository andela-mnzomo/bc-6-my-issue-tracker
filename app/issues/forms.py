from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SelectField, SubmitField, StringField, PasswordField, BooleanField, ValidationError, validators

from ..models import db, User, Issue, Department

class IssueForm(Form):
  ''' Form for users to raise an issue '''
  
  subject = StringField('Issue Subject',
                       [validators.Required(message='Please enter a subject for your issue.'),
                        validators.Length(
                           max=80,
                           message='Your subject should be brief.'
                       )
                       ]
                       )
  description = TextAreaField('Issue Description',
                              [validators.required(
                                  message='Please describe your issue.')])
  priority = SelectField('Priority', choices=[
      ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])
  department = SelectField('Department',
                           [validators.Required(
                               message='Department required.')],
                           coerce=int)
  submit = SubmitField('Post Issue')

  def __init__(self, *args, **kwargs):
      super(IssueForm, self).__init__(*args, **kwargs)
      self.department.choices = [
          (dept.id, dept.name) for dept in Department.query.all()]