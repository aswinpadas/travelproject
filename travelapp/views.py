from django.http import HttpResponse
from django.shortcuts import render
from . models import place,blog

# Create your views he
def fun(req):
    obj=place.objects.all()
    return render(req,"index.html",{'results':obj})
    #return HttpResponse("Hello World")
def funBlogRender(req):
    obj_blog=blog.objects.all()
    return render(req,"index.html", {'blog_results':obj_blog})