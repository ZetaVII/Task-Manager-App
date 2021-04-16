from app import db

class User(db.Model):
    """
    
    """
    

    """
    Output name of user.
    """
    def __repr__(self):
        return f'<User {self.username}>'



# Need to have tables created in order to access this form
db.create_all()
