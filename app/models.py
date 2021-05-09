from app import db
from datetime import datetime
from datetime import date
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

shares = db.Table('shares',
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                  db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
                  #db.Column('task_priority', db.Integer, db.ForeignKey('task.priority'))
                  )

class User(UserMixin, db.Model):
    """
    Set up table with user information.
    
    Attributes
    ----------
    id : Integer column
        Id of user.
    username : String column
        Username of user.
    password : String column
        Password of user.
    tasks : Query of tasks
        All of the tasks the user has access to.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False, unique=False)
    tasks = db.relationship('Task', secondary=shares, backref=db.backref('users', lazy='dynamic'))

    """
    Output name of user.
    """
    def __repr__(self):
        return f'<User {self.username}>'

class Task(UserMixin, db.Model):
    """
    Set up table with task information.

    Attributes
    ----------
    id : Integer column
        Id of task.
    title : String column
        Title of task.
    description : String column
        Description of the task.
    user_id : Integer column
        Id of user who created the task.
    complete : Integer column
        1 for complete and 0 for incomplete.
    deadline : String column
        Date that the task needs to be finished by.
    priority : Integer column
        priority of task needed.
    Reminder: Boolean Column
        Set a boolean to flash a reminder to finish a certain task.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=True, unique=False)
    # know which account the task belongs to
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # Set up column for complete status
    complete = db.Column(db.Integer)
    # Setting up one column for deadline
    deadline = db.Column(db.String, nullable=True, unique=False)
    # Create column for reminder
    reminder = db.Column(db.Boolean, nullable=False, default = False, unique=False)
    # Create column for remaining days
    #remaining_days = db.Column(db.String, Nullable = True, unique = False)
    # Create column for priority
    priority = db.Column(db.Integer, nullable=True, unique=False)
    # Create column for category
    category = db.Column(db.String, nullable=True, unique=False)
    
    
    def setDeadline(self, date):
        """
        Assign a deadline to a task.
        
        This function allows for the date to be set after the task is created.
        
        Parameters
        ----------
        date : string
            Date that the task needs to be done by.
        """
        self.deadline = date      
      
    def setPriority(self, priority):
        """
        Assign a priority to a task.
        
        This function allows for the priority to be set after the task is created.
        
        Parameters
        ----------
        priority : integer
            priority of the task.
        """
        self.priority = priority
        
        
    def addCategory(self, category):
        """
        Assign a category to a task.
        
        This function allows for the category to be added to task.
        
        Parameters
        ----------
        category : string
            category of the task.
        """
        self.category = category
        
    
    def setReminder(self, reminder):
        """
        Sets a reminder to a flash a message whenever the user logs in.

        Parameters 
        ----------
        reminder : boolean
            reminder attribute of task
        """
        self.reminder = reminder
    
    def setCompleteStatus(self, status):
        """
        Sets the complete status of the task.

        Parameters
        ----------
        status : int
            1 for complete and 0 for incomplete.
        """
        self.complete = status        

    """
    Output name of task.
    """
    def __repr__(self):
        return f'<Task {self.title}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))    
    
# Need to have tables created in order to access this form
db.create_all()
