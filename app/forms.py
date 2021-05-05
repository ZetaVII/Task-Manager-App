from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """
    Represents the form for logging in.
    Attributes
    ----------
    username : StringField
        Text box for user to enter username.    
    password : PasswordField
        Text box for user to enter password.
    submit : SubmitField
        Button for user to log in.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class OverviewForm(FlaskForm):
    """
    Represent the form for the account home page.

    Attributes
    ----------
    complete : BooleanField
        Checkbox for user to mark task as complete.
    createtask : SubmitField
        Button to make a new task.
    deletetask : SubmitField
        Button to delete a task.
    """
    complete = BooleanField('Mark as complete')
    createtask = SubmitField('Create Task')
    deletetask = SubmitField('Delete Task')

class NewTaskForm(FlaskForm):
    """
    Represents the form for creating a new task.

    Attributes
    ----------
    title : StringField
        Where users can type in the title of a new task. Data is required for this.
    description : StringField
        Where users can type in the description of a new task. Data is not required for this.
    create : SubmitField
        Button for user to finish creating new task.
    date : StringField
        Where users can type in a date for a deadline of a task. Data is not required for this.
    """
    title = StringField('Title', validators = [DataRequired()])
    description = StringField('Description')
    create = SubmitField('Create')
    date = DateField('Finish by (mm/dd/yyyy)', format=('%m/%d/%Y'))

class DeleteTaskForm(FlaskForm):
    """
    Represents the form for deleting a task.
    
    Attributes
    ----------
    title : StringField
        Where users can type in the title of a task that they will delete. Data is required for this.
    delete : SubmitField
        Button for user to finish deleting a task.
    """
    title = StringField('Title of task to delete', validators = [DataRequired()])
    delete = SubmitField('Delete')

class RegisterForm(FlaskForm):
    """
    Represents the form for creating a new user account.
    Attributes
    ----------
    username : StringField
        Text box for user to enter username.    
    password : PasswordField
        Text box for user to enter password.
    create : SubmitField
        Button for new user to make an account.
    """
    username = StringField("Username", validators= [DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    create = SubmitField("Register")
    
class EditTaskForm(FlaskForm):
    """
    Represents the form for editing an existing task.

    Attributes
    ----------
    title : StringField
        Textbox for user to enter a new title.
    description : StringField
        Textbox for user to enter a new title.
    save : SubmitField
        Button for user to save changes.
    """
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description")
    save = SubmitField("Save changes")

class FindTaskForm(FlaskForm):
    """
    Represents the form for finding an existing task.

    Attributes
    ----------
    title : StringField
        Title of the task.
    find : SubmitField
        Button for user to start search for task by title.
    """
    title = StringField("Title", validators=[DataRequired()])
    find = SubmitField("Find")

class ShareTaskForm(FlaskForm):
    """
    Represents the form for sharing a task with another user.

    Attributes
    ----------
    title : StringField
        Title of the task being shared.
    username : StringField
        Username of the recipient user.
    share : SubmitField
        Button for the user to share the task with another user.
    """
    title = StringField("Task", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    share = SubmitField("Share")    

    
 class SetPriorityForm(FlaskForm):
    """
    Represents the form for setting priority to a task.

    Attributes
    ----------
    title : StringField
        Title of the task being shared.
    priority : IntegerField
        priority number of the task.
    set : SubmitField
        Button for the user to set priority of a task.
    """
    title = StringField("Task", validators=[DataRequired()])
    priority = IntegerField("Priority", validators=[DataRequired()])
    set = SubmitField("Set")    
    
    
