from django.db import models

# Create your models here.
class place(models.Models):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)