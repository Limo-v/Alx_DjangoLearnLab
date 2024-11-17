from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title is required.')
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError('Author is required.')
        return author

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError('Description is required.')
        return description
