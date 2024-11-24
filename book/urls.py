from django.urls import path

from .views import APIMoviesView, Search_movie, SortByPrice, DetailView


urlpatterns = [
    path('', APIMoviesView.as_view(), name="home"),
    path('search/', Search_movie.as_view(), name="search"),
    path('sort/', SortByPrice.as_view(), name="sort"),
    path('<int:pk>/', DetailView.as_view(), name="detail"),

]
