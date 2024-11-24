from django.db import models
from django.contrib.auth.models import User

from book.models import Movie

class CartItem(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.movie.movie_name}'
    
    def __len__(self):
        return self.quantity