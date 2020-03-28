from django.db import models

# Create your models here.

class Disease(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

class City(models.Model):
    name = models.CharField(max_length=80)
    population = models.CharField(max_length=12, default='')
    territory = models.CharField(max_length=50)
    connected_cities = models.ManyToManyField('self')
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)


class Card(models.Model):
    title = models.CharField(default='', max_length=50)
    description = models.CharField(default='', max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    is_event = models.BooleanField(default=False)
    is_epidemic = models.BooleanField(default=False)




