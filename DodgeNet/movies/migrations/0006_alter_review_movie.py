# Generated by Django 5.0 on 2023-12-13 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_review_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Movie'),
        ),
    ]
