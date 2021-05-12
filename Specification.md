# URL to Team Repository 
* https://github.com/schau-sjsu/Team3.git

# Team Members
* Stephanie Chau: schau-sjsu
* Kevin La: ZetaVII
* Ethan DeGuzman: eth4nd
* Kassandra Dominguez: kdominguez49

# Use Case Description
**Product Name:** Task Manager

**Problem Statement:** Allow users to organize daily tasks in a convenient and accessible way. 

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
 * All system message prompts have a response time within 1 second after its trigger.
 * The "Sign up" button is represented by a colorful and clearly visible box.

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
 * All system message prompts have a response time within 1 second after its trigger.
 * The "Log in" button is represented by a colorful and clearly visible box.

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
User selects the "Create Task" button.

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
 * All system message prompts have a response time within 1 second after its trigger.
 * The "Create" button is represented by a colorful and clearly visible box.

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
1. System prompts the user to type in the name of a task.
2. The user enters a title and presses the "Find" button.
3. System redirects the user to the Editing page.
4. User clicks on the field that they wish to edit.
5. User types changes to title or description.
6. User clicks the "Save changes" button.
7. System redirects the user to the overview page.

### Primary Postconditions
* The user should be back at the overview page.
* Changes to the task are reflected in the list on the overview page.

### Alternate Sequences
1. The user enters a a task that doesn't exist.
	1. The user clicks the "Find" button.
	2. System prompts the user to enter a different title.
2. The user deletes the contents of the title field without typing a new title.
	1. The user clicks on the "Save changes" button.
	2. System prompts the user to enter a title.

### Alternate Trigger
User clicks the "Save changes" button after deleting the contents of the title field.

### Alternate Postconditions
 * The user remains on the Editing page.
 * Changes to the task are not saved.

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 
 * All system message prompts have a response time within 1 second after its trigger.
 * The "Save changes" button is represented by a colorful and clearly visible box.

### Glossary
* user = a person with an existing account and at least one task who wants to edit a task.

## **Use Case 5 Name:** Delete a task

### Summary
A person with an existing account can delete any tasks that they had previously created.

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* The user must have at least one existing task. 

### Triggers
User selects the "Delete task" button.

### Primary Sequence
1. System redirects the user to the delete task page.
2. System prompts user to type in the title of task to delete.
3. The user clicks on "Delete" to save changes.
4. System redirects the user to the overview page.

### Primary Postconditions
* The user should be back at the overview page.
* Updates to the task list are reflected on the overview page.

### Alternate Sequences
1. The user does not select a task to delete.
	1. The user clicks on the "Delete" button.
	2. System prompts the user to select a task to delete.

### Alternate Trigger
User clicks the "Delete" button after not selecting any task to be deleted.

### Alternate Postconditions
 * The user remains on the Delete task page.
 * Updates to the task list are not saved.

### Non-functional Requirements
 *  System prompt messages are presented with a font size between 20 and 24.
 *  All system message prompts have a response time within 1 second after its trigger.
 *  The "Delete" button is represented by a colorful and clearly visible box.

### Glossary
* user = a person with an existing account and at least one task, who wants to delete a task.

## **Use Case 6 Name:** Sign out

### Summary
A person with an existing account can sign out of the app.

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* The user must be already logged into the app. 

### Triggers
User selects the "Log out" button.

### Primary Sequence
1. User clicks the "Log out" button.
2. System redirects the user to the Login page. 

### Primary Postconditions
* The user should be back at the Login page.

### Non-functional Requirements
 *  System prompt messages are presented with a font size between 20 and 24.
 *  All system message prompts have a response time within 1 second after its trigger.
 *  The "Log out" button is represented by a colorful and clearly visible box.

### Glossary
* user = a person with an existing account who is already logged into the app, that is trying to log out.

## **Use Case 7 Name:** Add deadline for a task 

### Summary
A person with an existing account can add a deadline to complete a task.

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* The user must have at least one existing task. 

### Triggers
User enters deadline date.

### Primary Sequence
1. System prompts the user to select one task from the list.
2. The user selects an existing task from the displayed list.
3. System prompts user to type in a deadline date for the task.
4. The user types in the date into the prompt.
5. User clicks on the "Save changes" button.
6. System redirects the user to the overview page.

### Primary Postconditions
* The user should be back at the overview page.
* Task list now displays the deadline of each tasked created.
* Task list is now reordered by most recent deadline date in overview page.

### Alternate Sequences
1. The user does not type in a deadline date into the prompt.
	1. The user clicks on the "Save changes" button.
	2. System prompts the user to enter a date.

### Alternate Trigger
User clicks the "Save changes" button after not typing in any deadline date.

### Alternate Postconditions
 * The user remains on the Add deadline to task page.
 * Updates to the task list are not saved.

### Non-functional Requirements
 *  System prompt messages are presented with a font size between 20 and 24.
 *  All system message prompts have a response time within 1 second after its trigger.
 *  Deadline format should be easy to follow.
 *  The "Save changes" button is represented by a colorful and clearly visible box.

### Glossary
* user = a person with an existing account and at least one task, who wants to add a deadline date to a task.

## **Use Case 8 Name:** Add time duration for a task 

### Summary
A person with an existing account can add a time duration to complete a task.

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* The user must have at least one existing task. 

### Triggers
User selects a task from the task list, that they will currently work on.

### Primary Sequence
1. System prompts the user to add a time limit for this task.
2. The user types in a specific time into the prompt.
3. User clicks on the "Enter" button.

### Primary Postconditions
* Chosen task is now updated with a corresponding estimated time of completion.

### Alternate Sequences
1. The user does not type in a specific time into the prompt.
	1. The user clicks on the "Enter" button.
	2. System prompts the user to enter a time duration.

### Alternate Trigger
User clicks the "Enter" button after not typing in any time duration.

### Alternate Postconditions
 * The user is still prompted to add a time duration for the chosen task.
 * Updates to the task list are not saved.

### Non-functional Requirements
 *  System prompt messages are presented with a font size between 20 and 24.
 *  All system message prompts have a response time within 1 second after its trigger.
 *  The "Enter" button is represented by a colorful and clearly visible box.

### Glossary
* user = a person with an existing account and at least one task, who wants to add a time duration to a task.

## **Use Case 9 Name:** Mark task complete 
### Summary
User who is logged in can mark a task complete and will be added to the completed task list.

### Actors
1. The user

### Preconditions
* User is signed in.
* User has incomplete tasks.

### Triggers
User clicks “mark task complete” button.

### Primary Sequence
1. User clicks on task they wish to complete.
2. User clicks “mark task complete” button.
3. User clicks the "Save" button.
4. System refreshes the page and shows task appended to the completed tasks list.

### Primary Postconditions
* Task is marked complete.
* Task details are hidden.
* Tast title is marked with strike through.

### Alternate Sequences
1. User clicks on task they wish to complete.
2. User clicks “mark task complete” button.
3. Check if task is incomplete.
4. If already completed app shows error “task already completed”.

### Alternate Postconditions
 * App shows “task already completed”.
 
### Non-functional Requirements
 *  System prompt messages are presented with a font size between 20 and 24.
 *  All system message prompts have a response time within 1 second after its trigger.
 *  The "Save changes" button is represented by a colorful and clearly visible box.
### Glossary
* user = has registered username and password
* task = item user entered on to do list

## **Use Case 10 Name:** View completed tasks
### Summary
User who is logged in can view all complete tasks.

### Actors
1. The user

### Preconditions
* User is signed in.
* User has completed tasks.

### Triggers
User checks the checkbox to mark task as complete and clicks "Save" button.

### Primary Sequence
1. User checks checkbox to mark task as complete.
2. User clicks the "Save" button.
3. Checks if task is complete.
4. Adds task to completed task list. 
5. App shows “completed tasks”.

### Primary Postconditions
* Completed tasks are shown.

### Alternate Sequences
1. User clicks on "Save button".
2. If no completed tasks, then app displays nothing in "completed tasks".

### Alternate Postconditions
* App shows no completed tasks.

### Non-functional Requirements
 *  System prompt messages are presented with a font size between 20 and 24.
 *  All system message prompts have a response time within 1 second after its trigger.
 *  The "Save changes" button is represented by a colorful and clearly visible box.

### Glossary
* user = has registered username and password
* task = item user entered on to do list

## **Use Case 11 Name:** View incomplete tasks

### Summary
User who is logged in can view all incomplete tasks.

### Actors
1. The user

### Preconditions
* User is signed in.
* User has incomplete tasks.

### Triggers
User creates a task.

### Primary Sequence
1. User creates a task.
2. User adds task to incomplete task list. 
3. App updates “Incomplete Tasks”.

### Primary Postconditions
* Incomplete tasks are shown.

### Alternate Sequences
1. User creates a task.
2. User marks the task as complete.
3. User clicks the "Save" button.
4. Removes task from incomplete tasks list. 
5. App updates “Incomplete Tasks”.

### Alternate Postconditions
App shows “Incomplete Tasks”.
 
### Non-functional Requirements
 *  System prompt messages are presented with a font size between 20 and 24.
 *  All system message prompts have a response time within 1 second after its trigger.
 *  The "Save changes" button is represented by a colorful and clearly visible box.

### Glossary
* user = has registered username and password
* task = item user entered on to do list

## Use Case 12 Name: Set Priority of Tasks 

### Summary
Users are able to assign the priority level, such as high (needs to be done ASAP), to a certain task and put them at the top of the lists.

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* A task must be in progress of creation, or created beforehand.

### Triggers
User selects the “Set Priority” option.

### Primary Sequence
1. The user creates a new task, or selects an existing one.
2. The user clicks on the “Set Priority” button.
3. System prompts user levels of priority.
4. The user enters a priority level.

### Primary Postconditions
* The specified task should given priority listed.

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 
 * All system message prompts have a response time within 1 second after its trigger.

### Glossary
* user = a person with an existing account who is trying to log in.

## Use Case 13 Name: Categorize Task 

### Summary
Users are able to assign tasks into separate categories (ie. school, work, or personal life). 

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* A task must be in progress of creation, or created beforehand.

### Triggers
User selects the “CATEGORY” option.

### Primary Sequence
1. The user creates a new task, or enters an existing task.
2. The user clicks on the “CATEGORY” button.
3. System prompts the user to enter or create a new category.
4. The user selects an option.

### Primary Postconditions
* The specified task would be shown within the proper category within a list.

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 
 * All system message prompts have a response time within 1 second after its trigger.

### Glossary
* user = a person with an existing account who is trying to log in.

## Use Case 14 Name: Set Reminder 

### Summary
Users are able to have the server to set a flashy message to remind them to do a certain task(s).

### Actors
1. The user

### Preconditions
* The user must be previously registered.
* A task must be in progress of creation, or created beforehand.

### Triggers
User selects the “SET REMINDER” option.

### Primary Sequence
1. System prompts user list of tasks.
2. The user creates a new task, or selects an existing one.
3. he user checkmar the on the “FLASH REMINDER” button.
4. System prompts the user how many days left before the deadline of the task.

### Primary Postconditions
* There will be a flashy message in red underneath the specified task to remind the user.

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 
 * All system message prompts have a response time within 1 second after its trigger.

### Glossary
* user = a person with an existing account who is trying to log in.

## Use Case 15 Name: Share Task 

### Summary
Users can share tasks with other users to collaborate with one another.

### Actors
1. Two or more users

### Preconditions
* At least two users must be previously registered.
* There must be a pre-existing task within a list. 

### Triggers
User selects the “Share Task” option.

### Primary Sequence
1. System prompts user to enter in task title and username of recipient user.
3. The user enters information to both fields.
4. The user clicks on the “Share” button.
5. System reroutes to overview page. 
6. System alerts user of successful share.

### Primary Postconditions
* The selected task would be seen within the task manager of the two or more users.

### Alternate Sequences
1. User enters a title that does not exist.
	1. System prompts user to enter a different title.
2. User enters a username that does not exist.
 	1. System prompts user to enter a different username.

### Alternate Postconditions
App reloads share task page.

### Non-functional Requirements
 * System prompt messages are presented with a font size between 20 and 24. 
 * All system message prompts have a response time within 1 second after its trigger.
 * System alerts for shared users are sent within 5 seconds after sharing task.

### Glossary
* user = a person with an existing account who is trying to log in.

# Use Case Diagram
![image](https://user-images.githubusercontent.com/78886694/113962944-8cc1a680-97dd-11eb-97f2-0ba954505ce2.png)

