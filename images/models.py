from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.city

    def delete_location(self):
        self.delete()    

class Category(models.Model):
    name = models.CharField(max_length=20)

    def save_category(self):
        self.save()


    def __str__(self):
        return self.name

    def delete_category(self):
        self.delete()        
        
 
class Images(models.Model):
    image = models.ImageField(upload_to = 'photos',default = 'no photo')
    image_name = models.TextField()
    image_description = models.TextField()
    image_location = models.ForeignKey(Location,on_delete=CASCADE) 
    image_category = models.ForeignKey(Category,on_delete=CASCADE)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.save()
    
    @classmethod
    def search_by_category(cls,category):
        images=cls.objects.filter(image_category__name__icontains=category)
        return images


    