>>> book_to_retrieve = Book.objects.first()
>>> Book.objects.get
>>> print(book_to_retrieve.title, book_to_retrieve.author, book_to_retrieve.publication_year)
1984 George Orwell 1949
>>>