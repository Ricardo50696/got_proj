# Generated by Django 3.2.8 on 2021-10-31 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20211031_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodes',
            name='imdbRating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='imdb Rating'),
        ),
    ]