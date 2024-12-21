from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm

class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "users/register.html", context={"form":form})
    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken")
                return redirect("home")
            
            user_obj = form.save(commit=False)
            user_obj.set_password(password)
            user_obj.save()

            authenticate_user = authenticate(request, username=username, password=password)
            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect("home")
            
        return render(request, "users/register.html", context={"form":form})



class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', context={'form': form})
    
    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect("register")
            user_obj = authenticate(username=username, password=password)

            if user_obj:
                login(request, user_obj)
                return redirect("home")
            messages.error(request, "Wrong password")
            return redirect("login")
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect("home")


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")