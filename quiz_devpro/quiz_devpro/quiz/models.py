from django.db import models

# Create your models here.

class Game (models.Model):
    title = models.TextField()
    options = models.JSONField()
    available = models.BooleanField(default=False)
    answer = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])
