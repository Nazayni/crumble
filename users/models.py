from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='../assets/icons/user.png')
    bio = models.CharField(blank=True, max_length=250)
    links = models.TextField(blank=True, null=True)
    
    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='followers', 
        blank=True
    )
    
    def __str__(self):
        return f'{self.user.username} Profile'