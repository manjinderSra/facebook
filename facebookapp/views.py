from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(req):
    return render(req, 'home.html')

def register(req):
    if req.method == "POST":
        first = req.POST['first_name']
        last = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        User.objects.create_user(username=email, email=email, password=password, first_name=first, last_name=last)
        messages.success(req, "Account created successfully!")
        return redirect('login')
    return render(req, 'register.html')

def view_login(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user :
          login(req, user)
          return redirect('/')
        else:
            return redirect('login')
    return render(req,'login.html')

def user_logout(req):
    logout(req)
    return redirect('login')

def profile(req):
    if req.method == "POST":
        username = req.POST.get('username')
        image = req.FILES.get('image')
        user = User.objects(username=username, image=image)
        user.save()
        return redirect('profile')
    
    return render(req, 'profile.html')