# TaskShadow - Your tasks, always by your side.

![taskshadow-logo](https://github.com/user-attachments/assets/dc6e788f-40b2-450d-9da1-01aba3b927d1)

## Purpose and Target Audience

The purpose of TaskShadow is to provide an easy to use todo list with a clean interface with enough features to allow users to manage their work in a more efficient and time friendly manor.

## Target Audience:

TaskShadow is mainly aimed at adults who want to manage their workloads with ease!

## Problem Statement:

How can TaskShadow provide a good user experience for users looking to manage their todo lists?

## The Design
* Design was to be kept simple and easy for users to understand and use the application
* Design was also kept simple to keep the project managable within the time allocated
* The design, wireframes and other design elements can be seen below
https://miro.com/app/board/uXjVLwGurBo=/

## MVP Features

User Authentication:
* Secure user registration and login functionality.
* Password recovery options.

Adding Tasks:
* Create new tasks

Deleting tasks:
* Deleting current tasks

Admin Section will allow:
* Managing users
* Managing todo lists

Responsive Design:
* Mobile-friendly layout to ensure usability on various devices.

Privacy and Security:
* Data protection measures to safeguard user information.
* Compliance with privacy policies and terms of service.

## Future Features

Todo Lists:
* Allow drag and drop or reordering of list
* Update the style of the site to a more modern one
* Above should also allow it to be easier accessed on mobile
* Possibly add a priority rating on todo items, 1-10 or something with colours depending of level, 1 green - 10 red    

## User Stories:

* As a user, I want to create tasks with titles, descriptions, and deadlines so that I can organize my work efficiently.
* As a user, I want to mark tasks as completed so that I can track my progress.
* As a user, I want to edit task details so that I can update information if my plans change.
* As a user, I want to delete tasks so that I can remove tasks I no longer need.
* As a user, I want to categorize my tasks by priority or type so that I can focus on what's most important.

## Testing / Unit Testing:
* I used ChatGPT to write the tests for the TaskShadowTodo Model ensuring functionality is as expected

## User Registration and Login:
### User

* User navigates to the registration page.
  
* User enters email, password, and other required details.
  
* User submits the form.
  
* System sends a verification email.
  
* User verifies the email.
  
* User logs in with verified credentials.

### Users Table
| Attribute | Data Type   | Description      |
|-----------|-------------|------------------|
| UserID    | INT         | Primary Key      |
| Email     | VARCHAR(255)| Unique, Not Null |
| Password  | VARCHAR(255)| Not Null         |
| IsAdmin   | BOOLEAN     | Default FALSE    |

## Prioritized Features for MVP:

### User Authentication:

* Secure user registration and login functionality.
* Password recovery options.

### Responsive Design:

* Mobile-friendly layout to ensure usability on various devices.

### Privacy and Security:

* Data protection measures to safeguard user information.
* Compliance with privacy policies and terms of service.

## Future Enhancements (Post-MVP):

* Moving / reordering tasks
* Adding a priority rating on todo items, 1-10 or something with colours dependent of level, 1 green - 10 red

## Resources:
* https://miro.com/app/board/uXjVLwGurBo=/ - Miro board for planning and brainstorming

## Credits
* Logo: https://logo.com/
* Base code guide: https://www.youtube.com/watch?v=7tGZOq4ODNM
* ChatGPT: helped create the tests.py tests
* Bootstrap: Used for general styling
* Used ChatGPT to write the tests for the TaskShadowTodo Model

