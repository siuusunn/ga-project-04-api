from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pocket(models.Model):
    number_of_red_packets = models.IntegerField(default=0)
    items = models.ManyToManyField('items.Item', related_name="pockets")
    owner = models.ForeignKey("jwt_auth.User", related_name="pocket", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner}'s Pocket"
