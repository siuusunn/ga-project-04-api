from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class RedPackets(models.Model):
    number_of_red_packets = models.IntegerField(default=0)
    owner = models.ForeignKey("jwt_auth.User", related_name="number_of_red_packets", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner} - {self.number_of_red_packets}"
