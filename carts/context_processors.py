from .models import Cart, CartItem
from .views import _Cart_id

def counter(request):
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart_count = 0 
            cart = Cart.objects.filter(cart_id=_Cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity 
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)