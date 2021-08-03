from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

UserModel = get_user_model()


# Create your models here.

class Telescope(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='telescopes')
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} | {self.model}'


class Comment(models.Model):
    telescope = models.ForeignKey(Telescope, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.telescope.make} - {self.name}'


