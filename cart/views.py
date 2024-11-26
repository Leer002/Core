from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View

from .models import UserInfo

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


class CheckOut(View):
    def get(self, request):
        cart = request.session.get("cart")
        user = request.session.get("user", "")
        address = request.session.get("address", "")
        phone_number = request.session.get("phone_number", "")
        
        return render(request, "cart/checkout.html", {
            "cart": cart,
            "user": user,
            "address": address,
            "phone_number": phone_number
        })
    def post(self, request):
        user = request.POST.get("user")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")
        cart = request.session.get("cart")

       
        user_instance = request.user

        user_info, created = UserInfo.objects.get_or_create(user=user_instance)
        user_info.address = address
        user_info.phone_number = phone_number
        user_info.save()

        return render(request, "cart/checkout.html", {
            "user": user,
            "address": address,
            "phone_number": phone_number,
            "cart": cart,
            "status": "Successful"
        })
      

class InfosView(View):
    def get(self, request):
        user_info = UserInfo.objects.filter(user=request.user).first()
        
        name = request.user.username 
        phone = user_info.phone_number if user_info else ''
        address = user_info.address if user_info else ''
        
        return render(request, 'cart/infos.html', {
            'name': name,
            'phone': phone,
            'address': address,
            'status': 'Please enter your information.' if not phone else ''
        })

    def post(self, request):
        name = request.POST.get('name') 
        phone = request.POST.get('phone')
        address = request.POST.get('address')

    
        user_info, created = UserInfo.objects.get_or_create(user=request.user)

        
        user_info.phone_number = phone
        user_info.address = address
        user_info.save()

        return render(request, "cart/infos.html", {
            "name": name,  
            "phone": phone,
            "address": address,
            "status": "Successful"
        })

