from django.shortcuts import get_object_or_404
from photos.models import Photo
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_items = []
    total = 0
    for item_id, item_quantity in cart.items():
        this_photo = get_object_or_404(Photo, pk=item_id)
        this_total = this_photo.price * Decimal(item_quantity)
        total += this_total
        this_item = {
            'product_id': item_id, 
            'image': this_photo.image,
            'name': this_photo.name,
            'quantity': item_quantity,
            'price': this_photo.price,
            'total': this_total,
        }
        cart_items.append(this_item)

    return { 'cart_items': cart_items, 'total': total }