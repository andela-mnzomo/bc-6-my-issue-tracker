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

  # assigned_user = SelectField('User',
  #                          [validators.Required(
  #                              message='You must assign the issue to a person.')],
  #                          coerce=int)

  submit = SubmitField('Submit')

  def __init__(self, *args, **kwargs):
      super(IssueForm, self).__init__(*args, **kwargs)
      self.department.choices = [
          (dept.id, dept.name) for dept in Department.query.all()]
      # self.assigned_user.choices = [
      #     (assigned_user.id, assigned_user.fullname) for user in User.query.all()]

class CommentForm(Form):
  ''' Form for admins to add comment to issue '''
  
  comment = TextField("Add A Comment",  [validators.Required("Please enter a comment name.")])
