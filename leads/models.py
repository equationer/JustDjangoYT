from django.db import models
#from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Lead(models.Model):
    """'''
    SOURCE_CHOICES = (
        ('YouTube','YouTube'),
        ('Google','Google'),
        ('NewsLetter','NewsLetter'),

    )
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete = models.CASCADE)
    """
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    profile_picture = models.ImageField(blank=True, null = True)
    special_files= models.FileField(blank=True , null= True)
    """
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

