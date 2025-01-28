from django.db import models

# Create your models here.
class Posts(models.Model):
    #the fields relate to forms
    #for small amount of text
    title = models.CharField(max_length=75)
    #text area form input
    body = models.TextField()
    #identifies the posts or article
    slug = models.SlugField()
    #adds current time stamp of the post
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title