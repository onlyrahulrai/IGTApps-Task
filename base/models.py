from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)
    dob = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.username = self.name.strip().lower()
        return super(User,self).save(*args,**kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    front_img = models.ImageField(upload_to="front")
    back_img = models.ImageField(upload_to="back")
    self_image = models.ImageField(upload_to="profiles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.name