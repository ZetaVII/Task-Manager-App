from app import db
from app import login

class User(db.Model):
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
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False, unique=True)

    """
    Output name of user.
    """
    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):
    """
    Set up table with task information.

    Attributes
    ----------
    id : Integer column
        Id of task.
    title : String column
        Title of task.
    user_id : Integer column
        Id of user who created the task.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False, unique=True)
    # know which account the task belongs to
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # Setting up one column for deadline
    deadline = db.Column(db.String, db.ForeignKey("task.id"), nullable = True)

    def setDeadline(self, date):
        if date is NULL:
            return
        elif (int(date[0]) is not range(0,10) or int(date[1]) is not range(0,10)
            or int(date[3]) is not range(0,10) or int(date[4]) is not range(0,10)
            or int(date[6]) is not range(0,10) or int(date[7]) is not range(0,10)
            or int(date[8]) is not range(0,10) or int (date[9]) is not range(0,10)
            ):
            flash("Please enter valid date.")
        else:
            self.deadline = date


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

