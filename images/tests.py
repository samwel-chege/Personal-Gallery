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

class CategoryTestClass(TestCase):
    def setUp(self):
        self.name = Category(name = 'Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category)) 

    def test_save_method(self):
        self.name.save_category()
        categories = Location.objects.all()
        self.assertTrue(len(categories)>0)   


class ImagesTestClass(TestCase):
    def setUp(self):
        self.image = Images(image = 'image.jpg')          
