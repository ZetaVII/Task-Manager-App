from flask import render_template, redirect, session
from flask_login import login_required, logout_user

from app import db
from app import app
from app.forms import LoginForm, OverviewForm, NewTaskForm
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
    

@app.route('/createtask')
@login_required
def createtask():
    form = NewTaskForm()
    if form.validate_on_create():
        if title is None:
            flash('Please type in a title for new task')
            return redirect('/createtask')
        flash(f'New task created: {form.title.data}')
    return render_template('newtask.html', title='New Task', form=form)
    return redirect('/overview')
