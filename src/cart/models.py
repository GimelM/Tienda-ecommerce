from django.db import models
from store.models import Pets

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def Subtotal(self):
        return self.pet.price * self.quantity
        
    
    def __unicode__(self):
        return self.pet