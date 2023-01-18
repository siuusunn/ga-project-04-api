from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    item_image = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.name}"