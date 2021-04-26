from app import db

class User(db.Model):
    """
    
    """
    

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
    id : IntegerField
        Id of task.
    title : StringField
        Title of task.
    user_id : IntegerField
        Id of user who created the task.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    # know which account the task belongs to
    user_id = db.Column(db.Integer, db.ForeignKey(user.id))

    """
    Output name of task.
    """
    def __repr__(self):
        return f'<Task {self.title}>'

# Need to have tables created in order to access this form
db.create_all()

