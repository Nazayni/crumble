from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    userpass = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)