from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=300)
    number_of_red_packets = models.IntegerField(default=0)
    items = models.ManyToManyField('items.Item', related_name="items", default=4)
    multiplier = models.IntegerField(default=1)

