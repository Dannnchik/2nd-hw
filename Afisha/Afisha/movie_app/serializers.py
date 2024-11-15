from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']

class MovieWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'rating']

class DirectorWithMoviesCountSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

