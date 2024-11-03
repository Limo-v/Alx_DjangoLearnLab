>>> # Delete created book
>>> book_to_retrieve.delete()
(1, {'bookshelf.Book': 1})
>>> # Check if book has been deleted
>>> all_books = Book.objects.all()
>>> print(all_books)
<QuerySet []>
>>> 
