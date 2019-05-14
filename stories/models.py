from django.db import models
from django.contrib.auth.admin import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profile_picture = models.FileField()
    bio = models.TextField()


    def __str__(self):
        return self.name

class Resources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


    def __str__(self): return self.resource_name




