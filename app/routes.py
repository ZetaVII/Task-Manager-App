from flask import render_template, redirect, session, flash
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

from app import db
from app import app
from app.forms import LoginForm, OverviewForm, NewTaskForm, DeleteTaskForm, RegisterForm
# Make sure to import all tables
from app.models import User, Task

@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Registers new user by creating username and password
    """
    form = RegisterForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None:
            newuser = User(username=form.username.data, password=form.password.data)
            db.session.add(newuser)
            db.session.commit()
            flash('Success!')
            return redirect('/login')
        flash('User already exists')
        return redirect('/login')
    return render_template("register.html", title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
@app.route("/")
def login():
    """
    Logs in user with existing username and password
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('No account found')
            return redirect('/login')
        if not user.password == form.password.data:
            flash('Incorrect password')
            return redirect('/login')
        login_user(user)
        return redirect('/overview')
    
    return render_template("login.html", title="SIGN IN", form=form)

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
    

@app.route('/createtask', methods = ['GET', 'POST'])
@login_required
def createtask():
    """
    Creates a new task.
    
    User will return to the overview page once finished creating task
    User remains on createtask page if all fields required are not filled out.

    Returns
    -------
    Redirect to the createtask page.
    Redirect to the overview page.
    Render the newtask.html template.
    """
    form = NewTaskForm()
    if form.validate_on_submit():
        
        if form.title.data is None:
            flash('Please type in a title for new task')
            return redirect('/createtask')
        else:
            newtasks = Task(title=form.title.data)
            newtasks.setDeadline(form.date.data)
            db.session.add(newtasks)
            db.session.commit()
        return redirect('/overview')
        flash(f'New task created: {form.title.data}')
    return render_template('newtask.html', title='New Task', form=form)

@app.route('/deletetask', methods = ['GET', 'POST'])
@login_required
def deletetask():
    """
    Deletes a task.

    User will return to the overview page once finsihed deleting a task.
    User remains on the deletetask if all the fields required are not filled out.

    Returns
    -------
    Redirect to the deletetask page.
    Redirect to the overview page.
    Render the deletetask.html template.
    """
    form = DeleteTaskForm()
    if form.validate_on_submit():
        if form.title.data is None:
            flash('Please type in a title of task to delete')
            return redirect('/deletetask')
        else:
            deletedtask = Task.query.filter_by(title=form.title.data).first()
            db.session.delete(deletedtask)
            db.session.commit()
        return redirect('/overview')
        flash(f'Task deleted: {form.title.data}')
    return render_template('deletetask.html', title='Delete Task', form=form)
