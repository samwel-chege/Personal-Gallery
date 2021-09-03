from django.db import models
from django.db.models.expressions import F

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=20)
        
 
class Images(models.Model):
    image = models.ImageField(upload_to = 'photos')
    image_name = models.TextField()
    image_description = models.TextField()
    image_location = models.ManyToManyField(Location) 
    image_category = models.ManyToManyField(Category)

    

    