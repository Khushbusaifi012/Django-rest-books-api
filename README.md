"# Django-rest-books-api" 
# Book API - Django REST Framework

## Overview

The **Book API** is a simple application built using **Django** and **Django REST Framework** to manage a collection of books. This API allows you to perform CRUD (Create, Read, Update, Delete) operations for books in a database.

The API includes endpoints to:
- Retrieve a list of all books.
- Add a new book.
- Get details of a single book.
- Update book details.
- Delete a book.

## Features

- Full CRUD functionality for books.
- Easy to integrate with front-end applications or other systems.
- Built using **Django** for backend logic and **Django REST Framework** for creating the API endpoints.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django REST Framework**: A powerful toolkit and Endpoint for building Web APIs.
- **SQLite**: Default lightweight database (can be switched to PostgreSQL, MySQL, etc.).
- **Python**: Programming language for the backend.

## Installation

Follow the steps below to set up this project locally:-

1.pip install django djangorestframework

2.python -m django createproject project  (for make a project)

3.cd project

4.python manage.py createapp api   (for make a app)

5.Create a model in models.py according to your need.

6.Create a file in api.py named at serializers.py(to convert data into json form)

7.Then write down code in views.py according to your requirements.

8.Create a new file called urls.py inside the api app folder and define the endpoints.

9.Include the api URLs in the Project's urls.py

10.Apply the migrations to create the database schema for the Book model:

i) python manage.py makemigrations

ii) python manage.py migrate

11.Run the Development Server(python manage.py runserver)

12.http://127.0.0.1:8000/api/books/

(For Example) Body json format:
{
  "title": "New Book Title",
  "author": "Author Name",
  "published_date": "date"
}

13.Retrun json data:
[
    {
        "id": 1,
        "title": "Wings of Fire",
        "author": "A.P.J Abdul Kalam",
        "published_date": "1999-01-01"
    }

  ]
  
14.And if you want to add this data into admin panel then u create a superuser on this command:
(python manage.py createsuperuser)

15. Access the Admin Panel (http://127.0.0.1:8000/admin/) Same data show into on this.
16. Also I have make a html page to add a data through on this page.
  
