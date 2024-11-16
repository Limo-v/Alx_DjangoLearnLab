from django.shortcuts import render
from django.shortcuts import render
from .models import Book
from .models import Library

from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        return render(request, 'relationship_app/library_detail.html', {'library': library})
