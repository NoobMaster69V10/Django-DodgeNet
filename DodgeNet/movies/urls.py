from django.urls import path

from .views import AllView, MovieDetailView, MoviesView, SeriesDetailView, SeriesView, AddMovieReview, ActorsView, AddSeriesReview

urlpatterns = [
    path("", AllView.as_view()),
    path("movies/<slug:slug>", MovieDetailView.as_view(), name="movie_detail"),
    path("series/<slug:slug>", SeriesDetailView.as_view(), name="series_detail"),
    path("movies/", MoviesView.as_view(), name="category_movies_detail"),
    path("series/", SeriesView.as_view(), name="category_series_detail"),
    path("review/movie/<int:pk>", AddMovieReview.as_view(), name="add_movie_review"),
    path("review/series/<int:pk>", AddSeriesReview.as_view(), name="add_series_review"),
    path("actors/", ActorsView.as_view(), name="actors_detail")
]
