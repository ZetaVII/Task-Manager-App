from flask import render_template, redirect, session, flash, url_for, request
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from datetime import datetime

from app import app
from app import db
from app.forms import LoginForm, OverviewForm, NewTaskForm, DeleteTaskForm, RegisterForm, FindTaskForm, EditTaskForm, ShareTaskForm, SetPriorityForm, CategorizeForm
# Make sure to import all tables
from app.models import User, Task

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registers new user by creating username and password
    
    Returns
    -------
    Render the register.html template.
    Redirect to the register page. 
    Redirect to the login page.
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
@app.route("/", methods=['GET', 'POST'])
def login():
    """
    Logs in user with existing username and password.
    
    Returns
    -------
    Render the login.html template.
    Redirect to the overview page. 
    Redirect to the login page.
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
    
    return render_template("login.html", title="Sign In", form=form)

@app.route('/overview', methods=['GET', 'POST'])
@login_required
def overview():
    """
    Create the account overview page.

    Display all existing tasks in a list. Provide options for creating, deleting, and
    editing tasks along with other options for interacting with tasks.
   
    Also displays the completed/incomplete tasks, and updates these lists if a task gets marked as complete.

    Returns
    -------
    Render the overview.html template.
    Redirect to the overview page. 
    """
    form = OverviewForm()
    if request.method == 'GET':        
        taskList = []
        completedTasks = []
        uncompletedTasks = []
        format = "%b-%d-%Y"
        buttondisplay = {}
        if len(current_user.tasks) != 0:
            buttondisplay["show"] = True
        for task in current_user.tasks:
            due_by = datetime.strptime(task.deadline, format) - datetime.now()

            if task.reminder == 1:
                taskList.append({"Title": task.title, "Reminder": True, "Deadline": task.deadline, "Due_By": due_by.days, 
                                 "ID": task.id, "Priority": task.priority})
                uncompletedTasks.append({"Title":task.title})
            else:
                taskList.append({"Title": task.title, "Deadline": task.deadline, "ID": task.id, "Priority": task.priority})
                uncompletedTasks.append({"Title":task.title})

            if task.priority != 11:
                for dict in taskList:
                    if dict["Title"] == task.title:
                        dict["PriorityExists"] = dict["Priority"]

            if task.category != "":
                for dict in taskList:
                    if dict["Title"] == task.title:
                        dict["Category"] = task.category

            if task.complete == 1:
                completedTasks.append({"Title":task.title})
                for dict in taskList:
                    if dict["Title"] == task.title:
                        dict["Complete"] = task.complete
                uncompletedTasks.remove({"Title":task.title})
        taskList.sort(key=lambda i: (i["Priority"] is None, i["Priority"]))   
        return render_template('overview.html', title='Account Overview', form=form, list=taskList, 
                               completedTasks=completedTasks, uncompletedTasks=uncompletedTasks, buttondisplay=buttondisplay)
    
    elif request.method == 'POST':
        if request.form['submit'] == "clear":
            for task in current_user.tasks:
                db.session.delete(task)
            db.session.commit()
        if request.form['submit'] == "save":
            checks = request.form.getlist('check')
            for key in checks:
                t = Task.query.get(key)
                t.setCompleteStatus(1)
                t.priority = None
                db.session.commit()
        return redirect('/overview')

@app.route('/logout', methods=['GET', 'POST'])
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
    Title and finish by date required

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

        t = Task.query.filter_by(title=form.title.data).first()
        if t is not None:
            flash('Task already exists.')
            return redirect('/createtask')
        
        else:
            newtasks = Task(title=form.title.data, user_id=current_user.id, reminder = form.reminder.data)
            newtasks.setDeadline(form.date.data.strftime("%b-%d-%Y"))

        if form.description.data is not None:
            newtasks.description = form.description.data
        
        if form.priority.data is not None:
            newtasks.priority = form.priority.data
        else:
            newtasks.priority = 11
        
        if form.category.data is not None:
            newtasks.category = form.category.data

        current_user.tasks.append(newtasks)
        db.session.add(newtasks)
        db.session.commit()

        return redirect('/overview')
        flash('New task created')
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
        elif form.title.data is not None:
            t = Task.query.filter_by(title=form.title.data).first()
            if t is None:
                flash("Task does not exist!")
                return redirect('/deletetask')
            else:
                db.session.delete(t)
                db.session.commit()
                return redirect('/overview')
                flash('Task deleted')
    return render_template('deletetask.html', title='Delete Task', form=form)

@app.route('/edittask', methods=['GET', 'POST'])
@login_required
def editTask():
    """
    Edits a task.

    User remains on the edittask if no title is entered for the task that you want to make edits for. 
    User remains on the edittask if the title is already taken. 
    User will return to the overview page once finished editing a task.
    
    Returns
    -------
    Redirect to the edittask page.
    Redirect to the overview page.
    Render the edittask.html template. 
    """
 
    form = EditTaskForm()
    task = session.get('task', None)
    tk = Task.query.filter_by(title=task).first()
    if form.validate_on_submit():
        if form.title.data is None:
            flash('Enter a title')
            return redirect('/edittask')
        t = Task.query.filter_by(title=form.title.data).first()
        if t is not None:
            flash('Title already taken.')
            return redirect('/edittask')
        tk.title = form.title.data
        tk.reminder = form.reminder.data
        if form.description.data is not None:
            tk.description = form.description.data
        db.session.commit()
        return redirect('/overview')
    return render_template('edittask.html', title='Edit Task', form=form)

@app.route('/setpriority', methods=['GET', 'POST'])
@login_required
def setPriority():
    """
    Sets the priority of a given task.
    
    User remains on the setpriority if no title is entered for the task.
    User remains on the setpriority if a priority number is not specified. 
    User remains on the setpriority if title of task entered does not exist. 
    User will return to the overview page once finished setting priority for a task.

    Returns
    -------
    Redirect to the setpriority page.
    Redirect to the overview page.
    Render the setpriority.html template. 
    """

    form = SetPriorityForm()
    #task = session.get('task', None)
    tt = Task.query.filter_by(title=form.title.data).first()
    if form.validate_on_submit():
        if form.title.data is None:
            flash('Enter title to set priority')
            return redirect('/setpriority')
        if form.priority.data is None:
            flash('Enter priority')
            return redirect('/setpriority')
        elif form.title.data is not None:
            if tt is None:
                flash("Task does not exist!")
                return redirect('/setpriority')
            elif form.priority.data is not None:
                tt.priority = form.priority.data
                #db.session.add(tt.priority)
                db.session.commit()
                return redirect('/overview')
                flash('Priority set!')
    return render_template('setpriority.html', title='Set Priority', form=form)
#no flash messages pop up when testing

@app.route('/setcategory', methods=['GET', 'POST'])
@login_required
def setCategory():
    """
    Sets a category for a given task.

    User remains on the setcategory if title of task entered does not exits..
    User will return to the overview page once finished setting category for a task.

    Returns
    -------
    Redirect to the setcategory page.
    Redirect to the overview page.
    Render the setcategory.html template.
    """

    form = CategorizeForm()
    tt = Task.query.filter_by(title=form.title.data).first()   
    if form.validate_on_submit():
        if tt is None:
            flash("Task does not exist!")
            return redirect('/setcategory')   
        else:
            tt.category = form.category.data
            db.session.commit()
            return redirect('/overview')
            flash('Category set!')
    return render_template('setcategory.html', title='Set Category', form=form)


@app.route('/findtask', methods=['GET', 'POST'])
@login_required
def findTask():
    """
    Finds a task.
    
    User will be able to search for a task by title. This is used for choosing a task to edit.
    
    Returns
    -------
    Redirect to Edit Task page.
    Redirect to Find Task page.
    Render the findtask.html template.
    """
    form = FindTaskForm()
    if form.validate_on_submit():
        if form.title.data is None:
            flash('Enter a title')
            return redirect('/findtask')
        t = Task.query.filter_by(title=form.title.data).first()
        if t is None:
            flash("No task found")
            return redirect('/findtask')
        session['task'] = t.title
        return redirect(url_for('editTask'))
    return render_template("/findtask.html", title='Find Task', form=form)

@app.route('/share', methods=['GET', 'POST'])
@login_required
def shareTask():
    """
    Shares a task with another user.
    
    Recipient user will also share editing and deleting capabilities over the task.
    
    Returns
    -------
    Redirect to the share task page.
    Redirect to the overview page.
    Renders the share.html template.
    """
    form = ShareTaskForm()
    if form.validate_on_submit():
        if form.title.data is None:
            flash("Enter a task to share")
            return redirect('/share')
        if form.username.data is None:
            flash("Enter a user to share with")
        t = Task.query.filter_by(title=form.title.data).first()
        u = User.query.filter_by(username=form.username.data).first()
        if t is None:
            flash("Task does not exist")
            return redirect('/share')
        if u is None:
            flash("User does not exist")
            return redirect('/share')
        u.tasks.append(t)
        db.session.commit()
        flash("Successful share")
        return redirect("/overview")
    return render_template("/share.html", title='Share Task', form=form)
