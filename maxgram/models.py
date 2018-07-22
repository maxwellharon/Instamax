from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


# Create your models here.
