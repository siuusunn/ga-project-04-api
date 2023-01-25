from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    item_image = models.CharField(max_length=300)
    red_packets_needed_to_unlock = models.IntegerField(default=1)
    multiplier = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


# python3 manage.py dumpdata items --output items/seeds.json --indent=2;