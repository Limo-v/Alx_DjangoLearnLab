from django.shortcuts import render
from django.shortcuts import render
from .models import Book, Library
from django.views import View

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(View):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        return render(request, 'library_detail.html', {'library': library})
