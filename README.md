# Task Manager

Use this app to create and organize tasks. Keep tasks personal or share with other users for collaborative tasks.

## Table of Contents

* [Technologies](#technologies)
* [Installation](#installation)
* [Features](#features)
  * [Log in](#log-in)
  * [Log out](#log-in)
  * [Register new user](#register-new-user)
  * [Create new task](#create-new-task)
  * [Delete task](#delete-task)
  * [Mark task as complete](#mark-task-as-complete)
  * [Set deadline for task](#set-deadline-for-task)
  * [Edit a taks](#edit-a-task)
  * [Add time duration for a task](#add-time-duration-for-a-task)
  * [View completed tasks](#view-completed-tasks)
  * [View incomplete tasks](#view-incomplete-tasks)
  * [Set priority of tasks](#set-priority-of-tasks)
  * [Categorize task](#categorize-task)
  * [Set reminder](#set-reminder)
  * [Share task](#share-task)
* [Gantt chart](#gantt-chart) 

## Technologies

* Flask 1.1.2
* WTForms 2.3.3
* Flask-SQLAlchemy 2.4.4
* SQLAlchemy 1.3.23
* Werkzeug 1.0.1
* Python 3.9.2

## Installation

Minimum requirements:
* Have a version of python at least as recent as 3.0
* Have the above mentioned python libraries installed

Run this project by downloading the files within this repository. 
Navigate to the terminal and run the following:
```
$ cd ../Team3
$ python run.py
```

## Features

Use these features to access and personalize your tasks. 

### Log in

Use case 2: Log in

A person with an existing account can log in to the app.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-2-name-login)

Steps taken to ensure functionality:
* Test if user created in register in is still able to log in
* Ensure user is able to access pages
* Ensure user log out is successful
* Test account that has not been registered should not be able to log in

### Log out

Use case 6: Sign out

A person with an existing account can sign out of the app.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-6-name-sign-out)

Steps taken to ensure functionality:
* Create log out code in a simpler app.
* Test simpler app to ensure this section of the code works as expected.
  * Make sure logged out user cannot access account specific pages. 
* Test actual app once all prerequisite features are implemented. 

### Register new user

Use case 1: Register new user

A person can sign up by providing valid account details.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-1-name-register-new-user)

Steps taken to ensure functionality:
* Create new user account 
* Ensure that user is able to log in 
* Ensure user is able to access pages
* Ensure user log out is successful

### Create new task

Use case 3: Create a new task

A person can add a new task with a mandatory title and finish by date and optional description.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-3-name-create-a-new-task)

Steps taken to ensure functionality:
* Verify user not allowed to create a task with no title, description, date
* Verify user not allowed to create a task with no title, description
* Verify user not allowed to create a task with no description, date
* Verify user not allowed to create a task with no title, date
* Verify user not allowed to create a task with no title
* Verify user not allowed to create a task with no date
* Verify user not allowed to create a task with no description
* Verify user can to create a task with title, description, date


### Delete task

Use case 5: Delete a task

A person with an existing account can delete any tasks that they had previously created.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-5-name-delete-a-task)

Steps taken to ensure functionality:
* Delete existing task
* Ensure it is removed 
* Delete task that does not exist
* Ensure flash shows
* Ensure nothing happpens when text box empty 

### Mark task as complete

Use case 9: Mark task complete

User who is logged in can mark a task as complete.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-9-name-mark-task-complete)

Steps taken to ensure functionality:
* Create checkbox code in a simpler app.
* Test simpler app to ensure this section of the code works as expected.
  * Refresh the page to make sure checked boxes do not get reset.
* Test actual app once all prerequisite features are implemented. 

### Set deadline for task

Use case 7: Add deadline for a task

A person with an existing account can add a deadline to complete a task.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-7-name-add-deadline-for-a-task)

Steps taken to ensure functionality:
* Create input box within task creation in a simpler app
* Test simpler app to ensure this section of the code works as expected.
* Test actual app once all prerequisite features are implemented. 

### Edit a task

Use case 4: Edit a task

A person with an existing account can make edits to tasks they previously created.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-4-name-edit-a-task)

Steps taken to ensure functionality:
* Flash messages to page when forms are submitted
* Flash name of task to ensure that the correct task was selected
* Check to make sure edits are reflected on the overview page

### Add time duration for a task

Use case 8: Add time duration for a task

A person with an existing account can add a time duration to complete a task.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-8-name-add-time-duration-for-a-task)

Steps taken to ensure functionality:
* 

### View completed tasks

Use case 10: View completed tasks

User who is logged in can view all complete tasks.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-10-name-view-completed-tasks)

Steps taken to ensure functionality:
* 
### View incomplete tasks

Use case 11: View incomplete tasks

User who is logged in can view all incomplete tasks.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-11-name-view-incomplete-tasks)

Steps taken to ensure functionality:
* 
### Set Priority of Tasks

Use case 12: Set priority of tasks

Users are able to assign the priority level, such as high (needs to be done ASAP), to a certain task and put them at the top of the lists.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-12-name-set-priority-of-tasks)

Steps taken to ensure functionality:
* 
### Categorize Task

Use case 13: Categorize task

Users are able to assign tasks into separate categories (ie. school, work, or personal life).

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-13-name-categorize-task)

Steps taken to ensure functionality:
* 
### Set Reminder

Use case 14: Set task reminder

Users are able to have the system to send a notification to remind them to do a certain task(s).

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-14-name-set-reminder)

Steps taken to ensure functionality:
* 
### Share Task

Use case 15: Share task 

Users can share tasks with other users to collaborate with one another.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-15-name-share-task)

Steps taken to ensure functionality:
* Create new user
* Log out and create new user
* Log in and create new task
* Share task with first user
* Log out and log back in to recipient user
* Check to see if the shared task is present
* Edit newly shared task and save changes
* Log out and log in to other user
* Check if new changes are present

## Gantt chart

![image](https://user-images.githubusercontent.com/78131171/116381805-16a3d480-a7ca-11eb-8ec2-49bd19d6bea7.png)
