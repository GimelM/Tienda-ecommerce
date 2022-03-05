from multiprocessing import context
from django.shortcuts import redirect, render
from store.models import Pets
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, pet_id):
    pet = Pets.objects.get(id=pet_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(pet=pet, cart=cart,)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(pet = pet, quantity = 1, cart = cart,)
        cart_item.save()
        
    return redirect('cart')



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.pet.price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
        
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, "store/cart.html", context)
