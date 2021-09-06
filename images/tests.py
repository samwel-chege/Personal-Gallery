from django.test import TestCase
from .models import Location,Images,Category

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.city = Location(city = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.city,Location))  

    def test_save_method(self):
        self.city.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0) 

    def test_delete_method(self):
        self.city.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)       

class CategoryTestClass(TestCase):
    def setUp(self):
        self.name = Category(name = 'Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category)) 

    def test_save_method(self):
        self.name.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)   

    def test_delete_method(self):
        self.name.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)==0)     


class ImagesTestClass(TestCase):
    def setUp(self):
        self.image = Images(image = 'image.jpg') 
        self.image_category = Category(name = 'nature')    
        self.image_category.save_category()

        self.image_location = Location(city = 'Denver')
        self.image_location.save_location()

        self.image = Images(id=1,image_name = 'car',image_description = 'sports car',image_location = 'Nairobi',image_category = 'vehicles')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Images)) 

    def test_save_method(self):
        self.image.save_image()
        saved = Images.objects.all()
        self.assertTrue(len(saved)>0)

    def test_delete_method(self):
        self.image.delete_image()
        deleted = Images.objects.all()
        self.assertTrue(len(deleted)==0)   

    def test_search_method(self):
        image_category = 'car'
        searched = self.image.search_by_category(image_category)
        self.assertTrue(len(searched)>=0)                 
