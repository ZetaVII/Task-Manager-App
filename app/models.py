from app import db

class User(db.Model):
    """
    Attributes
    ----------
    username : StringField
        Users username
    password : StringField
        Users password
    user_id : IntegerField
        Id of user
    """
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False, unique=True)

    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password) 
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

# Need to have tables created in order to access this form
db.create_all()

