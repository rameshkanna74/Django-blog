from uuid import uuid4
from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.CharField(
        max_length=100,
        default=uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    artist = models.CharField(max_length=200, default="Artist")
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=400)
    image = models.URLField(max_length=400)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created"]
