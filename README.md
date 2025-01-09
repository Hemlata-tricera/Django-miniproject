# Django-miniproject

## Description
A simple bookstore application built using Django. This project allows users to browse and purchase books online. It includes features such as user authentication, a shopping cart, and an admin interface to manage the bookstore's inventory.

## Features
- User authentication (sign up, login, and logout)
- Search books
- Add books to the shopping cart
- Admin panel for managing books and users
  
## Installation Steps
1.	Create a Virtual Environment (if not already created):
   python -m venv venv
2.	Activate the Virtual Environment:
    venv\Scripts\activate
3.	Install Django:
     pip install Django
4.	Create a Django Project:
    django-admin startproject bookstore
    cd bookstore
5.	Create a Django App:
   python manage.py startapp store
6.	Configure Database
7.	Migrate the Database: python manage.py migrate
8.	Run the Development Server:
python manage.py runserver

### Prerequisites
Make sure you have the following installed on your machine:
asgiref==3.8.1
Django==5.1.4
Faker==33.3.0
python-dateutil==2.9.0.post0
six==1.17.0
sqlparse==0.5.3
typing_extensions==4.12.2
tzdata==2024.2
