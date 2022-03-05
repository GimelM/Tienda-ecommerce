from distutils.command.upload import upload
from django.db import models
from category.models import Category
from django.urls import reverse

class Pets(models.Model):
    pet_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/pets')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('pet_detail', args=[self.category.slug, self.slug])
    
    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.pet_name

    