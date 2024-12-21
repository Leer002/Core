from django.db import models

class Emenities(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_name =models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_image = models.ImageField(blank=True, null=True, upload_to="movies/")
    price = models.IntegerField()
    emenities = models.ManyToManyField(Emenities, blank=True)
    
    def __str__(self):
        return self.movie_name
    
    class Meta:
        db_table = 'movies'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

