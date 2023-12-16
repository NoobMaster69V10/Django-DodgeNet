from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *
from .forms import *


class AllView(View):
    """All View"""

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        series = Series.objects.filter(draft=False)
        return render(request, "movies/main-pg.html", {'movies': movies, 'series': series})


class MovieDetailView(DetailView):
    """Movie Detail View"""

    model = Movie
    slug_field = "url"
    template_name = "movies/movie.html"


class SeriesDetailView(DetailView):
    """Series Detail View"""

    model = Series
    slug_field = "url"
    template_name = "movies/series.html"


class MoviesView(View):
    """Movies View"""

    def get(self, request):
        info = Movie.objects.filter(draft=False)
        cat = Movie.objects.first()
        return render(request, "movies/category.html", {'info': info, 'cat': cat})


class SeriesView(View):
    """Series View"""

    def get(self, request):
        info = Series.objects.filter(draft=False)
        cat = Series.objects.first()
        form = ReviewForm()
        return render(request, "movies/category.html", {'info': info, 'cat': cat, 'form': form})


class AddMovieReview(View):
    """ Add Comment """

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(f"/movies/{movie.url}")


class AddSeriesReview(View):
    """ Add Comment """

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        series = Series.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.series = series
            form.save()
        return redirect(f"/series/{series.url}")


class ActorsView(ListView):
    """ Actors View """
    model = Actor
    template_name = "movies/actors.html"
    context_object_name = "actors"
