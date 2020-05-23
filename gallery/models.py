from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
  i_location = models.CharField(max_length=30, blank=True)

  def save_location(self):
    self.save()
  def delete_location(self):
    Location.objects.filter(pk=self.id).delete()

class Category(models.Model):
  i_category = models.CharField(max_length=30, blank=True)

  def save_category(self):
    self.save()
  def delete_category(self):
    Category.objects.filter(pk=self.id).delete()

class Image(models.Model):
  picture = models.ImageField(upload_to='')
  i_name = models.CharField(max_length=30)
  i_description = models.TextField()
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  up_date = models.DateTimeField(auto_now_add=True)

  def save_image(self):
    self.save()
  def delete_image(self):
    Image.objects.filter(pk=self.id).delete()