from django.http import HttpResponse
from django.shortcuts import render

# Create your views he
def fun(req):
    return render(req,"index.html")
    #return HttpResponse("Hello World")