# Task Management System (TMS)
 This is a Django-based Task Management System API that allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users.

# Features
 1. User Registration API
 2. Task Creation API
 3. Task Assignment API
 4. Retrieve Tasks for a Specific User

## Table of Contents

1. Technologies Used

2. Installation and Setup

3. API Endpoints

## Technologies Used

 1. Python: 3.12

 2. Django: 5.1

 3. Django rest framework: 3.15

 4. sqlite3


## Installation and Setup

> Create a virtual environment

- conda create -n venv python==3.12

- conda activate venv

- OR

- python -m venv venv

- source venv/bin/activate # On Windows: venv\Scripts\activate


> Clone the repository

- git clone 'https://github.com/skumar5011987/task_management_system.git'

- cd task_management_system


> Install the dependencies

- pip install -r requirements.txt


> Run migrations

- python manage.py makemigrations
- python manage.py migrate

> Create a Superuser (for Admin Access)

- either use:
 username = sam
 password = sam@123!
 
 OR

 Create your own
 python manage.py createsuperuser


> Start the development server

- python manage.py runserver


## API Endpoints

1.  User Registration

- URL: http://localhost:8000/api/register/
- Method: POST
- Request Body: 
 {
    "username": "john_doe",
    "email": "johndoe@example.com",
    "mobile": "9876543210",
    "gender": "male",
    "role": "manager",
    "password": "securepassword"
 }

- Response:
 {
    "id": 5,
    "username": "john_doe",
    "email": "johndoe@example.com",
    "gender": "male",
    "role": "manager",
    "mobile": "9876543210"
}

2. Create a Task

- URL: http://localhost:8000/api/tasks/
- Method: POST
- Request Body: 
 {
    "name": "Fix User Sign up flow",
    "description": "Users are unable to Sign up in due to incorrect data validation.",
    "task_type": "bug",
    "status": "pending"
 }

- Response:
 {
    "id": 4,
    "name": "Fix User Sign up flow",
    "description": "Users are unable to Sign up in due to incorrect data validation.",
    "task_type": "bug",
    "status": "pending",
    "blocked_reason": null,
    "created_at": "2025-03-25T13:00:19.718955Z",
    "completed_at": null
 }


3. Assign Task to User

- URL: http://127.0.0.1:8000/api/tasks/4/assign/
- Method: POST
- Request Body: 
 {
    "user_ids":[2,3]
 }

- Response:
 {
    "status": 1,
    "message": "Task assigned successfully"
 }


4. Get Tasks Assigned to a User

- URL: http://127.0.0.1:8000/api/users/{user_id}/tasks/
- Method: GET
- Response:
 {
    "message": "ok",
    "data": [
        {
            "id": 1,
            "name": "Fix Login Bug",
            "description": "Users are unable to log in due to incorrect token validation.",
            "task_type": "bug",
            "status": "pending",
            "blocked_reason": "",
            "created_at": "2025-03-25T11:19:28.160987Z",
            "completed_at": null
        },
        {
            "id": 3,
            "name": "Performance Optimization",
            "description": "Optimize database queries for faster performance.",
            "task_type": "task",
            "status": "pending",
            "blocked_reason": "",
            "created_at": "2025-03-25T11:21:53.967522Z",
            "completed_at": null
        }
    ]
 }


# Admin Panel Access

- URL: http://127.0.0.1:8000/admin/
- User credentials:
 username = sam
 password = sam@123!

OR 

- Login using your own superuser credentials created earlier.

