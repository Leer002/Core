# Generated by Django 4.2 on 2024-11-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
