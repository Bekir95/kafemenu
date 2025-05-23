from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    logo2 = models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tag = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # Menü görseli


    def __str__(self):
        return self.name