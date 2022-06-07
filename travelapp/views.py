from django.http import HttpResponse
from django.shortcuts import render
from travelapp.models import place, blog


def fun(req):
    obj = place.objects.all()
    obj_blog = blog.objects.all()
    # date=obj_blog.getDate()
    # Month = date.strftime("%B")
    # Day = date.strftime("%d")
    # obj_blog.setDate(Day,Month)
    # # day= obj_blog.date
    return render(req, "index.html", {'results': obj,'blog_results': obj_blog})
    # return HttpResponse("Hello World")


# def funBlogRender(req):
#     obj_blog = blog.objects.all()
#     print(obj_blog)
#     return render(req, "index.html", {'blog_results': obj_blog})
