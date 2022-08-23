from django.db import models

# Create your models here.
class Flower(models.Model):
    title = models.charField(max_length=255, default='')