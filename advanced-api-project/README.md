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

## Filtering, Searching, and Ordering

The API allows users to filter, search, and order books based on various criteria.

### Filtering
- **Filter by title**: `?title=Sample Book`
- **Filter by author**: `?author__name=John Doe`
- **Filter by publication year**: `?publication_year=2022`

### Searching
- **Search in title and author name**: `?search=Sample`

### Ordering
- **Order by title**: `?ordering=title`
- **Order by publication year**: `?ordering=publication_year`
- **Order by publication year descending**: `?ordering=-publication_year`