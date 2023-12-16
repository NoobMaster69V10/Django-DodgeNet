from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Categories"""
    name = models.CharField("Categories", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    """Actors"""
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor and director"
        verbose_name_plural = "Actors and directors"


class Genre(models.Model):
    """Genres"""
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    """Movies"""
    title = models.CharField("Title", max_length=150)
    tagline = models.CharField("Tagline", max_length=100, default="")
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Year of publication", default="")
    country = models.CharField("Country", max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name="Director", related_name="movie_director")
    actors = models.ManyToManyField(Actor, verbose_name="Actor", related_name="movie_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    budget = models.PositiveIntegerField("Budget", default=0, help_text="Amount of money in USD")
    fess_in_world = models.PositiveIntegerField("Fess in the world", default=0, help_text="Amount of money in USD")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})


class Series(models.Model):
    """Series"""
    title = models.CharField("Title", max_length=150)
    tagline = models.CharField("Tagline", max_length=100, default="")
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Year of publication", default="")
    country = models.CharField("Country", max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name="Director", related_name="series_director")
    actors = models.ManyToManyField(Actor, verbose_name="Actor", related_name="series_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    budget = models.PositiveIntegerField("Budget", default=0, help_text="Amount of money in USD")
    fess_in_world = models.PositiveIntegerField("Fess in the world", default=0, help_text="Amount of money in USD")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"

    def get_absolute_url(self):
        return reverse("series_detail", kwargs={"slug": self.url})


class MovieShots(models.Model):
    """Movie Shots"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie shot"
        verbose_name_plural = "Movie shots"


class RatingStar(models.Model):
    """Rating in stars"""
    value = models.SmallIntegerField("Value", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Rating star"
        verbose_name_plural = "Rating stars"


class Rating(models.Model):
    """Rating"""
    ip = models.CharField("IP Address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Star")
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name="Movie")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Review(models.Model):
    """Reviews"""
    name = models.CharField("Name", max_length=100)
    email = models.EmailField()
    text = models.TextField("Text", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Parents", on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE, null=True)
    series = models.ForeignKey(Series, verbose_name="Series", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
