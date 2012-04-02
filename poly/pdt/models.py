from django.db import models
from django.contrib import admin

class Family(models.Model):
    name = models.CharField(max_length=30)

class Genus(models.Model):
    name = models.CharField(max_length=30)

class Plant(models.Model):
    family = models.ForeignKey(Family)
    genus = models.ForeignKey(Genus)
    species = models.CharField(max_length=30)
    infraspecific_rank = models.CharField(max_length=30)
    infraspecific_epithet = models.CharField(max_length=30) 
    cultivar = models.CharField(max_length=30)


admin.site.register(Plant)


