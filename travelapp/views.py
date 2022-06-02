from django.http import HttpResponse
from django.shortcuts import render
from . models import place
# Create your views he
def fun(req):
    obj=place()
    obj.name='Kerala'
    obj.price=100
    obj.desc='God\'s Own country'

    return render(req,"index.html",{'result':obj})
    #return HttpResponse("Hello World")