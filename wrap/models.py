from django.db import models
from django.contrib.auth.models import User

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

    