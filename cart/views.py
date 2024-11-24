from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View

from .models import CartItem

from book.models import Movie

class CartItemView(View):
    def get(self, request):
        cart_items = request.session.get('cart', {})
        total_price = 0
        items_list = []
        total_quantity = sum(cart_items.values())  

        for movie_id, quantity in cart_items.items():
            movie = get_object_or_404(Movie, id=movie_id)
            total_price += movie.price * quantity
            items_list.append({'movie': movie, 'quantity': quantity})

        
        request.session['total_quantity'] = total_quantity
        request.session['cart'] = cart_items 
        return render(request, "cart/cart.html", {"cart_items": items_list, "total_price": total_price, "total_quantity": total_quantity})



class CartItemAddView(View):
    def post(self, request, movie_id):
        cart = request.session.get('cart', {})
        
        if str(movie_id) in cart:
            cart[str(movie_id)] += 1 
        else:
            cart[str(movie_id)] = 1 
        
        request.session['cart'] = cart 
        return redirect("cart-view")


class CartItemRemoveView(View):
    def post(self, request, movie_id):
        cart = request.session.get('cart', {})

        
        if str(movie_id) in cart:
            cart[str(movie_id)] -= 1
            
            
            if cart[str(movie_id)] <= 0:
                del cart[str(movie_id)]

        
        request.session['cart'] = cart  
        return redirect("cart-view")


