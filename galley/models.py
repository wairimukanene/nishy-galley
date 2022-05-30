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
    

  
  
class Photo(models.Model):
  category = models.ForeignKey(
  Category, on_delete=models.SET_NULL, null=True, blank=True)
  image= models.ImageField(null=False, blank=False)
  description = models.TextField()
  
  def __str__(self):
    return self.name
  
  def save_photo(self):
    self.save()
    
  def delete_image(self):
      self.delete()
  
  
  def __str__(self):
    return self.description
