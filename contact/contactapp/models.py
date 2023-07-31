from django.db import models

# Create your models here.
# Class contact(models.model):



class contactview(models.Model):
    fname=models.CharField(max_length=38)
    lname=models.CharField(max_length=38)
    phone=models.CharField(max_length=38)

    
 