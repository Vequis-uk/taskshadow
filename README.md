# TaskShadow - Your tasks, always by your side.


## Purpose and Target Audience

The purpose of TaskShadow is to provide an easy to use todo list with a clean interface with enough features to allow users to manage their work in a more efficient and time friendly manor.

## Target Audience:

TaskShadow is mainly aimed at adults who want to manage their workloads with ease!

## Problem Statement:

How can TaskShadow provide a good user experience for users looking to manage their todo lists?

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

## User Registration and Login:
### User

* User navigates to the registration page.
  
* User enters email, password, and other required details.
  
* User submits the form.
  
* System sends a verification email.
  
* User verifies the email.
  
* User logs in with verified credentials.

### Users Table                                  TODO UPDATE THIS
| Attribute | Data Type   | Description      |
|-----------|-------------|------------------|
| UserID    | INT         | Primary Key      |
| Email     | VARCHAR(255)| Unique, Not Null |
| Password  | VARCHAR(255)| Not Null         |
| IsAdmin   | BOOLEAN     | Default FALSE    |

### User Flow Diagram
```plaintext

TODO

```

## Prioritized Features for MVP:
###User Authentication:

* Secure user registration and login functionality.

* Password recovery options.

### Movie Database Management:

* Admin interface for adding, editing, and deleting movies.

* Basic movie details: title, year, director, brief description, and poster image.

### User Reviews and Ratings:

* Ability for users to submit reviews and ratings for movies.

* Display of average ratings and recent reviews on movie pages.

### Responsive Design:

* Mobile-friendly layout to ensure usability on various devices.

### Privacy and Security:

* Data protection measures to safeguard user information.

* Compliance with privacy policies and terms of service.

## Future Enhancements (Post-MVP):
* 



