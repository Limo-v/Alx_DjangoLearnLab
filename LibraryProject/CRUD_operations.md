CREATE
   command:
>>> from bookshelf.models import Book
>>> book = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()

   output:
No output
RETRIEVE
   command:
>>> book_to_retrieve = Book.objects.first()
>>> print(book_to_retrieve.title, book_to_retrieve.author, book_to_retrieve.publication_year)


   output:
1984 George Orwell 1949

UPDATE
   command:
>>> book_to_retrieve.title = "Nineteen Eighty-Four"
>>> book_to_retrieve.save()
>>> print(book_to_retrieve.title)


   output:
Nineteen Eighty-Four

DELETE
   command:
>>> book_to_retrieve.delete()
(1, {'bookshelf.Book': 1})
>>> # Check if book has been deleted
>>> all_books = Book.objects.all()
>>> print(all_books)


   output:
<QuerySet []>
