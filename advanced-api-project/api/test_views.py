rom rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework import status

class BookAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="John Doe")
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(title="Sample Book", publication_year=2022, author=self.author)
        self.client.login(username='testuser', password='testpass')

    def test_create_book(self):
        """Test creating a new book."""
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_update_book(self):
        """Test updating an existing book."""
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Updated Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        """Test deleting a book."""
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        """Test listing all books."""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books(self):
        """Test filtering books by title."""
        url = reverse('book-list') + '?title=Sample Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching books by title."""
        url = reverse('book-list') + '?search=Sample'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by title."""
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('Sample Book' in [book['title'] for book in response.data])