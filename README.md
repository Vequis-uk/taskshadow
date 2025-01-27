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
* Results of the tests can be seen below:

![image](https://github.com/user-attachments/assets/3af7cb4d-3044-4576-9d2c-5cd7fbe6f65b)

## Validation:
# https://validator.w3.org/ | Markup Validation Service
![image](https://github.com/user-attachments/assets/927a94c2-67ab-4b92-a2dc-8be98b719e98)

# https://jigsaw.w3.org/css-validator/ | CSS Validation Service
![image](https://github.com/user-attachments/assets/ac505a62-8755-4a84-80c6-b3358f3a38a7)

# https://pep8ci.herokuapp.com/ | CI Python Linter
![image](https://github.com/user-attachments/assets/4886b5ff-7bea-4e54-aeff-6402bd539c2f)
![image](https://github.com/user-attachments/assets/f5df70d9-3cba-4e3c-8017-691a2b3f84a4)
![image](https://github.com/user-attachments/assets/900449f3-6eca-4ea4-8a9d-ff8f3feb2078)
![image](https://github.com/user-attachments/assets/df48d53a-2752-46ff-ad19-9310012114d9)

# https://jshint.com/ | JS Validation


# https://wave.webaim.org/ | Web Accessibility Evaluation Tool
![image](https://github.com/user-attachments/assets/77fe671c-14e7-4a5e-b912-bfa776d10efa)


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

## AI Usage
* I used AI to help create the CSS styling for the popup messages for user feedback
* I used AI to write the tests for the TaskShadowTodo Model
* I used AI to help debug issues such as:
  * Issue with static files, where I had to remove and readd them as there was some sort of conflict
  * Issues with login redirecting when not required, the issue was due to a typo in my view registration
  * Heroku deployment issue due to gunicorn missing

## Credits
* Logo: https://logo.com/
* Base code guide: https://www.youtube.com/watch?v=7tGZOq4ODNM
* ChatGPT
* GitHub Copilot
* Bootstrap: Used for general styling

