from django.db import models
from django.db.models.expressions import F

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.city

class Category(models.Model):
    name = models.CharField(max_length=20)

    def save_category(self):
        self.save()


    def __str__(self):
        return self.name
        
 
class Images(models.Model):
    image = models.ImageField(upload_to = 'photos')
    image_name = models.TextField()
    image_description = models.TextField()
    image_location = models.ManyToManyField(Location) 
    image_category = models.ManyToManyField(Category)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.save()
    


    