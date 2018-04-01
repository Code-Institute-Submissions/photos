from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from photos.models import Photo
from decimal import Decimal
from cart.utils import get_cart_items_and_total
# Create your views here.

    
def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('photo_list')
    
def view_cart(request):
    
    cart = request.session.get('cart', {})
    print(cart)
    print(cart.items())
    context = get_cart_items_and_total(cart)
    print(context)
    return render(request, 'cart/view_cart.html', context)
    
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart') 