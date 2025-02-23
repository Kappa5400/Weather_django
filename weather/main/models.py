from django.db import models

# Create your models here.

class cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    coordinates = models.TextField()
    elevation = models.TextField()
    comment = models.TextField()
