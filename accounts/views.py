from django.core.mail import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

def login(req):
    if req.method=="POST":
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else :
            message.info(req,'invalid username or password')
            return redirect('login')
    else:
        return render(req,"login.html")
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
def logout(req):
    auth.logout(req)
    return  redirect('/')

# Create your views here.
