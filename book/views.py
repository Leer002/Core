from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View


from .models import Movie, Emenitites


class APIMoviesView(View):
    def get(self, request):
        movies_objs = Movie.objects.all()
        emenities = Emenitites.objects.all()
        total_quantity = request.session.get('total_quantity', 0)
        context = {"movies_objs":movies_objs, "emenities": emenities, "total_quantity": total_quantity, "user":request.user}
        return render(request, "book/base.html", context=context)
    
class Search_movie(View):
    def get(self, request):
        query = request.GET.get("query")
        if query:
            movies = Movie.objects.filter(movie_name__icontains=query)
        else:
            movies = Movie.objects.all()
        return render(request, 'book/search.html', context={"movies": movies, "query":query})
        

class SortByPrice(View):
    def get(self, request):
        price = request.GET.get("price")

        if price:
            movies = Movie.objects.filter(price__lte=price)
        else:
            movies = Movie.objects.all()
        return render(request, "book/sort.html", {"movies":movies, "price":price})


class DetailView(View):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            messages.error(request, "Not found")
            return redirect("home")
        return render(request, "book/detail.html", {"movie":movie})
