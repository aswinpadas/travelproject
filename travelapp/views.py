from django.http import HttpResponse
from django.shortcuts import render
from . models import place
# Create your views he
def fun(req):
    obj=place.objects.all()
    return render(req,"index.html",{'results':obj})
    #return HttpResponse("Hello World")
def funBlogRender(req):
    obj_blog = place.objects.all()
    print(obj_blog.day)
    render(req,"index.html", {'blog_results': obj_blog})