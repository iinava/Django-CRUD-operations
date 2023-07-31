from django.db import models

# Create your models here.
class studentview(models.Model):
    name=models.CharField(max_length=38)
    parent=models.CharField(max_length=38)
    contact=models.CharField(max_length=38)
    pincode=models.CharField(max_length=38)
    email=models.CharField(max_length=38)
    adress=models.CharField(max_length=38)



    