from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from photos.models import Photo
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required()    
def add_to_cart(request):
    id = request.POST['id']
    print("hello" + id)
    quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    request.session['cart'] = cart   
    return redirect('photo_list')
    
@login_required()     
def view_cart(request):
    cart = request.session.get('cart', {})
    print(cart)
    print(cart.items())
    context = get_cart_items_and_total(cart)
    return render(request, 'cart/view_cart.html', context)

@login_required()   
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart') 