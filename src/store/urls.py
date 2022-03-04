
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.store, name="store"),
    path('<slug:category_slug>', views.store, name="pets_by_category")

]
