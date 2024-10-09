from django.db import models

# Create your models here.
class Score(models.Model):
    yourname = models.CharField(max_length=200)
    mail = models.CharField(max_length=255)
    mobile = models.IntegerField(default=0)