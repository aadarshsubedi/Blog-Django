from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    img=models.ImageField(upload_to='category/',blank=True,null=True)
   
    def __str__(self):
        return self.title
class Blogs(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    img=models.ImageField(upload_to='blog/',blank=True,null=True)
    isfeatured=models.BooleanField(default=False)
    isSlider=models.BooleanField(default=False)
    
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
