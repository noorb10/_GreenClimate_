from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=200, null=True, default='') 
    profile_pic = models.ImageField(default="pfp.png",blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
