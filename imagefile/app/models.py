from django.db import models

# Create your models here.
class Notes(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='uploads/', null=True, blank =True)