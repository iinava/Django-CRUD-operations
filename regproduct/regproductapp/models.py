from django.db import models

# Create your models here.
class regview(models.Model):
    name=models.CharField(max_length=38)
    username=models.CharField(max_length=38)
    email=models.CharField(max_length=38)
    contact=models.CharField(max_length=38)
    password=models.CharField(max_length=38)
   


class regproduct(models.Model):
    ppname=models.CharField(max_length=38)
    pid=models.CharField(max_length=38)
    pcat=models.CharField(max_length=38)
    pprice=models.CharField(max_length=38)
