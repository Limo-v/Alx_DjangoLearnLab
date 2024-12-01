from django.db import models

class Author(models.Model):
    """
    Model for Author
    """
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model for book  that will be linked to an author
    """
    title = models.CharField(max_length=100)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Link to Author

    def __str__(self):
        return self.title