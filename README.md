# ProductivityLogger-using-Django

A Django-based productivity logger application that allows users to create tasks, log work sessions, and track the total time spent on each task. The application also checks if the tasks are completed within the specified time limit.

# Features

- **User Authentication**: Secure user login and registration.
- **Task Management**: Create, edit, delete, and view tasks.
- **Work Session Logging**: Log multiple work sessions for each task with start and end times.
- **Time Tracking**: Calculate the total time spent on tasks and check if the time limit is exceeded to decide productivity
- **Responsive Design**: Mobile-friendly interface using Bootstrap.

# Models

### Task

- **user**: ForeignKey to the `User` model
- **title**: CharField to store the task title
- **description**: TextField to store the task description (required)
- **time_limit**: DurationField to specify the allowed time for the task (required)
- **time_exceeded**: BooleanField to indicate if the time limit is exceeded
- **completed**: BooleanField to indicate if the task is completed

### WorkSession

- **task**: ForeignKey to the `Task` model
- **start_time**: DateTimeField to record the start time of the session
- **end_time**: DateTimeField to record the end time of the session

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Virtual environment tool (venv or virtualenv)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Parimal14121998/ProductivityLogger-using-Django.git
   cd productivity-logger

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   

5. **Create a superuser:**:
   ```bash
   python manage.py createsuperuser

   

6. **Run the development server**:
   ```bash
   python manage.py runserver

   

7. **Open your browser and navigate to**:
   ```bash
   http://127.0.0.1:8000

# Usage:- 
## Creating a Task
1. **Login**:
Use the Signup page to create a account and then signin OR 
Use the credentials created with the superuser command to login.

2. **Create a Task**:
Navigate to the task creation page.
Fill in the title, description, and time limit.
Submit the form to create the task.

## Logging Work Sessions
1. **Start a Work Session**:
Navigate to the task detail page.
Click on the "Start New Session" button to start logging time.
2. **End a Work Session**:
When you finish working, navigate back to the task detail page.
Click on the "End Session" button to stop logging time.

## Completing a Task
1. **Complete the Task**:
Navigate to the task detail page.
Click on the "Complete Task" button.
The system will check if the task is completed within the time limit and update the status accordingly.

## Running Tests
1. python manage.py test tasks

## Project Structure

productivity-logger/
│
├── productivity_logger/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── accounts/
│   │   ├── login.html
│   │   └── signup.html
│   ├── tasks/
│   │   ├── task_complete.html
│   │   ├── task_confirm_delete.html
│   │   ├── task_detail.html
│   │   ├── task_end_session.html
│   │   ├── task_form.html
│   │   ├── task_list.html
│   │   ├── task_start_session.html
│   │   └── base_generic.html
│
├── venv/
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt


   
