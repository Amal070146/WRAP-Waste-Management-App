from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

class Booking(models.Model):
    book_id=  models.AutoField(primary_key=True)
    wastetype = models.CharField(max_length=20)
    date = models.DateField(settings.DATE_FORMAT)
    typeaddress = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
   