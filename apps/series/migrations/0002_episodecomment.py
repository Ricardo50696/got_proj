# Generated by Django 3.2.8 on 2021-11-01 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpisodeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('episode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episode_comment', to='series.episodes')),
            ],
            options={
                'verbose_name': 'Episode Comment',
                'verbose_name_plural': 'Episode Comment',
            },
        ),
    ]
