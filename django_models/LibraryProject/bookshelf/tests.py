
# Delete created book
book_to_retrieve.delete()
# Check if book has been deleted
all_books = Book.objects.all()
print(all_books)