from django.db import models
from django.utils import timezone


class Movies(models.Model):

    GENRE_OPTIONS = (
        ('Horror', 'Horror'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('SciFi', 'SciFi'),
        ('Action', 'Action'),
        ('Period', 'Period')
    )
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=10,
                             choices=GENRE_OPTIONS)

    def __str__(self):
        return self.title