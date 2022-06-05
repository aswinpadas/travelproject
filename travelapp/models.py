from django.db import models
import datetime

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class blog(models.Model):
    date=models.DateField()
    # day=date.strftime("%d")
    # month=date.strftime("B")
    blog_img=models.ImageField(upload_to='pictures')
    news_post_title=models.CharField(max_length=50);
    news_post_category=models.CharField(max_length=30)
    news_post_content=models.TextField()
