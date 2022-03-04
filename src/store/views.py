from django.shortcuts import get_object_or_404, render
from store.models import Pets
from category.models import Category
    
def store(request, category_slug=None):
    
    categories = None
    pets = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        pets = Pets.objects.filter(category=categories, is_available=True)
        pet_count = pets.count
    else:
        pets = Pets.objects.all().filter(is_available=True)
        pet_count = pets.count()
    context = {
        'pets': pets,
        'pet_count': pet_count
    }
    return render(request, 'store/store.html', context)

