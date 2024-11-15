from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f'Review for {self.movie.title}'

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # от 1 до 5

    def __str__(self):
        return f'Review for {self.movie.title}'

class Review(models.Model):
    stars = models.IntegerField()