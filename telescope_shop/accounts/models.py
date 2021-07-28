from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

UserModel = get_user_model()


# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profiles', blank=True)
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.user.username}'


from .signals import *