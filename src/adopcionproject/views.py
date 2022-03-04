from django.shortcuts import render

from store.models import Pets

def home(request):
    pets = Pets.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'home.html', context)