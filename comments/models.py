from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("jwt_auth.User", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner} - {self.created_at}"



# python3 manage.py dumpdata items --output items/seeds.json --indent=2;