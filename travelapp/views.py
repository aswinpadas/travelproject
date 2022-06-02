from django.shortcuts import render

# Create your views he
def fun(req):
    return render(req,"home.html")