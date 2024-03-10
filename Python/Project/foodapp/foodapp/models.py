from django.db import models
from django.db import connection

# class details(models.Model):
#     email=models.CharField(max_length=120)
#     phone=models.CharField(max_length=120)
from django.db import models

class Details(models.Model):
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
class data(models.Model):
    name2=models.CharField(max_length=120)
    email2=models.CharField(max_length=120)
    phone2=models.CharField(max_length=120)

