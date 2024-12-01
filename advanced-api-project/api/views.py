
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    """List all books with filtering, searching, and ordering capabilities."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Fields to filter by
    search_fields = ['title', 'author__name']  # Fields to search in
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    Gets one book by ID
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]