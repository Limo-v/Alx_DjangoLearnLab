from django.urls import path
import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(template_name="library_detail"), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name="login")),
    path('logout/', views.LogoutView.as_view(template_name="logout")),
]