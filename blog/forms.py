from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    """ Movie Form """
    class Meta:
        """ Assigning the order of the fields"""
        model = Movies
        fields = ["title", "director", "genre", "language"]
