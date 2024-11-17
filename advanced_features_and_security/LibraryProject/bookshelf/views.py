from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .forms import ExampleForm # Assume you have a form for Book

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})