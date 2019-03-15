from django.db import models

# Create your models here.

class Hobbit(models.Model):

    name = models.CharField(max_length=60)
    breakfast = models.IntegerField(default=5)
    evil = models.BooleanField(default=False)
    ring = models.BooleanField(default=False)
    hungry = models.BooleanField(default=False)
    feet_size = models.FloatField(default=20.0)

    class Meta:
        db_table = 'Hobbit'
