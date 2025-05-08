from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    #the fields relate to forms
    #for small amount of text
    title = models.CharField(max_length=75)
    #text area form input
    body = models.TextField()
    #identifies the posts or article
    slug = models.SlugField()
    #adds current time stamp of the post
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title