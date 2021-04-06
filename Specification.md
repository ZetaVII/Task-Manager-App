# URL to Team Repository 
* https://github.com/schau-sjsu/Team3.git

# Team Members
* Stephanie Chau: schau-sjsu
* Kevin La: ZetaVII
* Howell Deguzman: eth4nd
* Kassandra Dominguez: kdominguez49

# Use Case Description
**Product Name:** Task Manager

**Problem Statement:**

**Date:** April 7, 2021

## **Use Case 1 Name:** Register new user

### Summary
A person can sign up by providing valid account details. 

### Actors
1. The new user

### Preconditions
* The new user must be on the Login page.

### Triggers
User selects the "Sign up" button.

### Primary Sequence
1. System redirects the user to the registration page.
2. System prompts the customer to enter a unique username and some password.
3. The new user types username and password into the respective fields.
4. The new user clicks the "Sign up" button.
5. System creates a new account with the new user's information.
6. System redirects the user to the Login page.
7. The user is notified of a successful registration.
8. System prompts the user to log in.

### Primary Postconditions. 
* A new account must exist with the provided username and password.
* The user should be back at the Login page.

### Alternate Sequences
1. The user enters a nonunique username.
	1. System prompts the user to enter a valid username. 
2. The user clicks the "Sign up" button without providing a username and/or password.
	1. System prompts the user to enter a username and/or password.

### Alternate Trigger
User clicks the "Sign up" button while username and/or password field is incomplete.

### Alternate Postconditions
 * The user is not taken back to the Login page.
 * No new account is made. 

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 

### Glossary
* new user = a person trying to make an account to be able to use the task manager app.

## **Use Case 2 Name:** Login

### Summary
A person with an existing account can log in to the app. 

### Actors
1. The user

### Preconditions
* The user must be previously registered.

### Triggers
User selects the "Log in" button.

### Primary Sequence
1. System redirects the user to the Login page.
3. System prompts the customer to enter their username and password.
4. The user types their username and password into the respective fields.
5. The new user clicks the "Log in" button.
6. System redirects the user to the overview page of their account.

### Primary Postconditions
* The user has access to their account.

### Alternate Sequences
1. The user enters a username that does not exist.
	1. System prompts the user to enter a valid username. 
2. The user enters an incorrect password.
	1. System prompts the user to enter the correct password..

### Alternate Trigger
User clicks the "Log in" button after giving mismatching username and password.

### Alternate Postconditions
 * The user remains on the Login page.
 * User is not given access to any account. 

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 

### Glossary
* user = a person with an existing account who is trying to log in.

## **Use Case 3 Name:** Create a new task

### Summary
A person can add a new task with a mandatory title and optional description.

### Actors
1. The user

### Preconditions
* The user must be logged into their account.
* The user must be on the overview page of their account.

### Triggers
User selects the "Create new task" button.

### Primary Sequence
1. System redirects the user to the New Task page.
2. System prompts the user to enter a title and description.
3. The user enters a title and description into the appropriate fields.
4. User clicks on the "Create" button. 
5. System redirects the user to the overview page.

### Primary Postconditions
* The user should be back at the overview page.
* The newly created task should be present in the list of tasks on the page.

### Alternate Sequences
1. The user clicks the "Create" button without entering a title.
	1. System prompts the user to enter a title. 

### Alternate Trigger
User clicks the "Create" button before specifying a title.

### Alternate Postconditions
 * The user remains on the New Task page.
 * No new task is created.

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 

### Glossary
* user = a person with an existing account trying to create a new task.

## **Use Case 4 Name:** Edit a task

### Summary
A person with an existing account can make edits to tasks they previously created.

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* The user must have at least one existing task. 

### Triggers
User selects the "Edit task" button.

### Primary Sequence
1. System prompts the user to select one task from the list.
2. The user selects an existing task from the displayed list.
3. System redirects the user to the Editing page.
4. User clicks on the field that they wish to edit.
5. User types changes to title or description.
6. User clicks the "Save changes" button.
7. System redirects the user to the overview page.

### Primary Postconditions
* The user should be back at the overview page.
* Changes to the task are reflected in the list on the overview page.

### Alternate Sequences
1. The user deletes the contents of the title field without typing a new title.
	1. The user clicks on the "Save changes" button.
	2. System prompts the user to enter a title.

### Alternate Trigger
User clicks the "Save changes" button after deleting the contents of the title field.

### Alternate Postconditions
 * The user remains on the Editing page.
 * Changes to the task are not saved.

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 

### Glossary
* user = a person with an existing account and at least one task who wants to edit a task.
