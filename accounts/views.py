from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

def register(req):
    if req.method =="POST":
        first_name=req.POST["first_name"]
        last_name=req.POST["last_name"]
        username=req.POST["username"]
        password1=req.POST["password1"]
        password2=req.POST["password2"]
        email=req.POST["email"]
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(req,'registration.html')

# Create your views here.
