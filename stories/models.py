from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profile_picture = models.FileField()
    bio = models.TextField()

class Resources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

