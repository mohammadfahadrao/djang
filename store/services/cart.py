from django.shortcuts import get_object_or_404, redirect
from store.models import Product, CartItem

def get_product_or_404(product_id):
    """
    Retrieve the product with the given ID from the database
    or return a 404 error if not found.
    """
    return get_object_or_404(Product, id=product_id)

def update_cart_item(product, user):
    """
    Update the cart item for the given product and user.
    """
    cart_item, created = CartItem.objects.get_or_create(product=product, user=user)
    cart_item.quantity += 1
    cart_item.save()

def add_to_cart(request, product_id):
    """
    Add a product to the cart and redirect to the cart view.
    """
    product = get_product_or_404(product_id)
    update_cart_item(product, request.user)
    return redirect('cart:view_cart')
