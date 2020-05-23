from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.wapi = Location(i_location='Ngong Hills')
  # Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.wapi,Location))
  # Testing Save method
  def test_save_method(self):
    self.wapi.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)>0)
  # Testing Delete method
  def test_delete_method(self):
    self.wapi.delete_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)<1)

class CategoryTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.category = Category(i_category='Landscape')
  # Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.category,Category))
  # Testing Save method
  def test_save_method(self):
    self.category.save_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)>0)
  # Testing Delete method
  def test_delete_method(self):
    self.category.delete_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)<1)

class ImageTestClass(TestCase):
  # Set up method
  def setUp(self):
    # Creating a location
    self.wapi = Location(i_location='Ngong Hills')
    self.wapi.save_location()
    # Creating a category
    self.category = Category(i_category='Landscape')
    self.category.save_category()
    # Creating an image
    self.picha = Image(i_name='The Rough Sea', i_description='Taken during the colonial days.', location=self.wapi, category=self.category)
  # Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.picha,Image))
  # Testing Save method
  def test_save_method(self):
    self.picha.save_image()
    pictures = Image.objects.all()
    self.assertTrue(len(pictures)>0)
  # Testing Delete method
  def test_delete_method(self):
    self.picha.delete_image()
    pictures = Image.objects.all()
    self.assertTrue(len(pictures)<1)