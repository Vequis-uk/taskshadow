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

* As a user, I want to be able to create an account
* As a user, I want to be able to login to my account
* As a user, I want to be able to add todos to a list
* As a user, I want to be able to set the priority of a todo when creating it
* As a user, I want to be able to mark my todos as complete
* As a user, I want to be able to delete todos
* As a user, I want to be able to set a priority on current todos
* As a user, I want to be able to log out of my account

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
![image](https://github.com/user-attachments/assets/f4f754dd-4258-4a09-ba2b-786c9a0ccfed)

# https://wave.webaim.org/ | Web Accessibility Evaluation Tool
![image](https://github.com/user-attachments/assets/77fe671c-14e7-4a5e-b912-bfa776d10efa)

# Lighthouse Testing
![image](https://github.com/user-attachments/assets/1577dc9d-7bbd-425e-bda6-4be1645fdd69)

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

## Deployment:
### 1. Install Required Packages
  * In your project folder:
    * pip install gunicorn psycopg2-binary whitenoise dj-database-url
  * Then add them to your requirements.txt:
    * pip freeze > requirements.txt
      
### 2. Update settings.py
* Add allowed hosts:
  * ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost', '127.0.0.1']
* Set up static files for production:
  * STATIC_ROOT = BASE_DIR / 'staticfiles'
  * STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
* Add middleware for WhiteNoise (for serving static files):
  * MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', ]

### 3. Create Procfile
* In the root of your project directory, create a file called Procfile (no extension), and add:
  * web: gunicorn taskshadow.wsgi (change project name accordingly, taskshadow in this case)

### 4. Initialize Git (if not already done)
* git init
* git add .
* git commit -m "Initial commit"

### 5. Create the Heroku App
* heroku login
* heroku create taskshadow (again, change name accordingly)

### 6. Set Config Vars
* heroku config:set SECRET_KEY='your-secret-key'
* heroku config:set DEBUG=False
* this can also be added in the settings on the Heroku webpage

### 7. Push to Heroku
* git push heroku master (change branch name accordingly)

### 8. Run Migrations and Collect Static Files
* heroku run python manage.py migrate
* heroku run python manage.py collectstatic --noinput

### 9. Visit The Site
* heroku open
* this can also be done via the heroku webpage

### If there are any issues see the webpage and look at the logs under more at the top right once you are inside the project.

# AI Usage
### 1. Code Creation and Enhancement
AI was instrumental in generating and refining several parts of the codebase, especially in areas where rapid prototyping and best practices were important:

### 2. CSS Styling for User Feedback Popups
I used ChatGPT to help create responsive and visually distinct CSS styles for popup messages that display user feedback (e.g., success, error, and warning messages). For instance, I was able to generate transition effects and styling templates that improved visibility while maintaining a non-intrusive UI experience. The AI suggested using @keyframes with subtle fade-ins and slide-ins, and helped fine-tune box shadows and color palettes that aligned with accessibility standards.

Example (from styles.css):

/* Editing to-do titles */

.edit-title-form {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.edit-title-input {
    border: 1px solid #ccc;
    padding: 0.3rem 0.5rem;
    border-radius: 5px;
    font-size: 1rem;
}

### New Form-Based Task Editing Feature
The introduction of a form-based approach for editing task titles was heavily assisted by ChatGPT. AI guided the restructuring of the frontend to support inline editing with form validation, and also helped refactor the backend view logic to process updates conditionally and handle errors gracefully.

ChatGPT provided suggestions on:

Django view logic (UpdateView)

HTML form structure

CSRF token handling

Preserving user input on failed submissions

### 2. Debugging and Troubleshooting
AI played a critical role in debugging several issues throughout the development process. Key examples include:

### Static Files Conflict
I encountered an issue where static files were not being served correctly due to a conflict caused by a previous misconfiguration. ChatGPT suggested clearing and re-adding the static files while checking the STATICFILES_DIRS and collectstatic flow, which ultimately resolved the issue.

### Login Redirection Bug
A typo in a view registration was causing unexpected login redirects. ChatGPT helped trace the problem by walking through the LOGIN_REDIRECT_URL logic and recommended using Django’s reverse_lazy for better URL management.

### Heroku Deployment Issue (Gunicorn)
An error related to gunicorn missing during deployment was resolved with AI assistance. It identified that gunicorn needed to be listed in requirements.txt and reminded me to include a Procfile. The fix involved running:

bash
Copy
Edit
pip install gunicorn
pip freeze > requirements.txt
echo "web: gunicorn myproject.wsgi" > Procfile
3. Automated Testing
TaskShadowTodo Model Tests
I used AI to write unit tests that covered edge cases and ensured the integrity of the TaskShadowTodo model. These included tests for:

Valid and invalid object creation

String representation

Checking field constraints like max length and nullability

Ensuring tasks are correctly associated with their respective users

Sample test generated with AI support:

python
Copy
Edit
def test_task_string_representation(self):
    task = TaskShadowTodo.objects.create(title="Buy Milk", user=self.user)
    self.assertEqual(str(task), "Buy Milk")
4. Code Optimization
ChatGPT was used to recommend optimizations in areas such as:

### Query Efficiency
Suggested the use of .select_related() and .prefetch_related() in views dealing with task-user relationships to reduce the number of database hits and improve performance.

### Form Handling and DRY Principles
Helped refactor repetitive form handling logic into reusable components. AI highlighted opportunities to extract common logic into mixins or utility functions.

### Responsive Design Improvements
AI recommended media query adjustments and utility-first CSS techniques to improve responsiveness without bloating the stylesheet.

### 5. Reflection on AI Integration
Using AI throughout this project drastically improved my development workflow. It served as a real-time pair programming assistant—offering not only direct solutions but also valuable explanations that helped me understand best practices.

The ability to debug faster, test more comprehensively, and style more confidently allowed me to maintain momentum without frequent context-switching to external documentation. Importantly, AI helped reinforce my understanding of Django and frontend principles through conversational learning.

# Credits
* Logo: https://logo.com/
* Base code guide: https://www.youtube.com/watch?v=7tGZOq4ODNM
* ChatGPT
* GitHub Copilot
* Bootstrap: Used for general styling

