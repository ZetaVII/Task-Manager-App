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
* NEEDS DEBUG CAUSES ERROR - Verify user not allowed to create a task with no description
* Verify user can to create a task with title, description, date


### Delete task

Use case 5: Delete a task

A person with an existing account can delete any tasks that they had previously created.

[Click here for the detailed use case description](https://github.com/schau-sjsu/Team3/blob/main/Specification.md#use-case-5-name-delete-a-task)

Steps taken to ensure functionality:
* [list steps here]

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

## Gantt chart

![image](https://user-images.githubusercontent.com/78131171/116381805-16a3d480-a7ca-11eb-8ec2-49bd19d6bea7.png)
