from django.urls import path
from .views import (
    DirectorWithMoviesCountView, MovieListView, MovieDetailView,
    MovieWithReviewsView, ReviewListView, ReviewDetailView
)

urlpatterns = [
    path('directors/', DirectorWithMoviesCountView.as_view(), name='director-list'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/reviews/', MovieWithReviewsView.as_view(), name='movie-with-reviews'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
