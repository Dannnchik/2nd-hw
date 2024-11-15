from django.db.models import Count
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Director, Movie, Review
from .serializers import (
    DirectorWithMoviesCountSerializer,
    MovieSerializer,
    MovieWithReviewsSerializer,
    ReviewSerializer
)
from django.db.models import Avg, Count


class DirectorWithMoviesCountView(ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movies'))
    serializer_class = DirectorWithMoviesCountSerializer

class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieWithReviewsView(ListAPIView):
    queryset = Movie.objects.annotate(rating=Avg('reviews__stars'))
    serializer_class = MovieWithReviewsSerializer

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
