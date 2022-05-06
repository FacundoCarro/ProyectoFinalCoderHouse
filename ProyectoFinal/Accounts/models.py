from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Avatar(models.Model):
    
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)