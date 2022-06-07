from django.db import models

# from x import datetime

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class blog(models.Model):
    date = models.DateField(null=True, blank=False)
    blog_img = models.ImageField(upload_to='pictures')
    news_post_title = models.CharField(max_length=50);
    news_post_category = models.CharField(max_length=30)
    news_post_content = models.TextField()
    # def getDate(self):
    #     return self.date
    # def setDate(self,d,m):
    #     self.day=d
    #     self.month=m
