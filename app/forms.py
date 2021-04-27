from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """
    
    """
    

class OverviewForm(FlaskForm):
    """
    Represent the form for the account home page.

    Attributes
    ----------
    logout : SubmitField
        Button for user to log out.
    complete : BooleanField
        Checkbox for user to mark task as complete.
    """
    logout = SubmitField('Log out')
    complete = BooleanField('Mark as complete')
    createtask = SubmitField('Create Task')
    deletetask = SubmitField('Delete Task')

class NewTaskForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    description = StringField('Description', validators = [DataRequired()])
    create = SubmitField('Create')
