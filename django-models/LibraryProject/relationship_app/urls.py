from django.urls import path
import views

urlpatterns = [
path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(template_name="library_detail"), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name="login")),
    path('logout/', views.LogoutView.as_view(template_name="logout")),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/', views.list_books, name='list_books'),

]