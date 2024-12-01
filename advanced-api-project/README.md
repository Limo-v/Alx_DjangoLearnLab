# Advanced API Project

## Overview
This project implements a RESTful API for managing books and authors using Django REST Framework.

## API Endpoints
- **GET /api/books/**: Retrieve a list of all books.
- **GET /api/books/<int:pk>/**: Retrieve details of a specific book by ID.
- **POST /api/books/create/**: Create a new book (authenticated users only).
- **PUT /api/books/update/<int:pk>/**: Update an existing book (authenticated users only).
- **DELETE /api/books/delete/<int:pk>/**: Delete a specific book (authenticated users only).

## Permissions
- List and detail views are accessible to all users.
- Create, update, and delete views are restricted to authenticated users.