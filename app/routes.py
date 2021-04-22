from flask import render_template, redirect, session
from flask_login import login_required, logout_user

from app import db
from app import app
from app.forms import LoginForm, OverviewForm
# Make sure to import all tables
from app.models import User, Task

@app.route("/", methods=['GET', 'POST'])
def login():
    """
    
    """
    form = LoginForm()

@app.route('/overview')
@login_required
def overview():
    """
    Create the account overview page.

    Display all existing tasks in a list. Provide options for creating, deleting, and
    editing tasks along with other options for interacting with tasks.

    Parameters
    ----------

    Returns
    -------
    Render the overview.html template.
    """
    form = OverviewForm()
    tasks = Task.query.all()
    list = []
    for task in tasks:
        list.append(task.title)
    return render_template('overview.html', title='Account Overview', form=form, list=list)

@app.route('/logout')
@login_required
def logout():
    """
    Log user out of account.

    User will be returned to the login page.
    
    Returns
    -------
    Redirect to the login page.
    """
    logout_user()
    return redirect('/')
    



