# Generated by Django 5.0 on 2023-12-13 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_actors_alter_movie_directors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movie_actor', to='movies.actor', verbose_name='Actor'),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Tagline')),
                ('description', models.TextField(verbose_name='Description')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default='', verbose_name='Year of publication')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('budget', models.PositiveIntegerField(default=0, help_text='Amount of money in USD', verbose_name='Budget')),
                ('fess_in_world', models.PositiveIntegerField(default=0, help_text='Amount of money in USD', verbose_name='Fess in the world')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('actors', models.ManyToManyField(related_name='series_actor', to='movies.actor', verbose_name='Actor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Category')),
                ('directors', models.ManyToManyField(related_name='series_director', to='movies.actor', verbose_name='Director')),
                ('genres', models.ManyToManyField(to='movies.genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
            },
        ),
    ]
