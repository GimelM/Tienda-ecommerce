from django.contrib import admin
from .models import Pets

class PetAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('pet_name',)}

admin.site.register(Pets, PetAdmin)

