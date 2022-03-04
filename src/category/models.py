from distutils.command.upload import upload
from enum import unique
from pyexpat import model
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=100,unique=True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank=True)
    
    def get_url(self):
        return reverse('pets_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name
    
