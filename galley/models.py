from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100, null=False,blank=False)
  
  def __str__(self):
    return self.name
  
  def save_name(self):
    self.save()
    
  def delete_name(self):
    self.delete()
    
    class Location(models.model):
      location=models.CharField(max_length=100)
      def __str__(self):
        return self.location
      
      
  @classmethod
  def get_locations(cls):
        locations = Location.objects.all()
        return locations

  @classmethod
  def update_location(cls, id, value):
        cls.objects.filter(id=id).update(photo=value)

  def save_location(self):
        self.save()

  def delete_location(self):
        self.delete()
  
  
class Photo(models.Model):
  category = models.ForeignKey(
  Category, on_delete=models.SET_NULL, null=True, blank=True)
  image= models.ImageField(null=False, blank=False)
  description = models.TextField()
  location = models.ForeignKey(Location,on_delete=models.SET_NULL, null=True, blank=True)
  
  def __str__(self):
    return self.description
