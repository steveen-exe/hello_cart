
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderedItem
from products.models import Product
from customers.models import Customer

def show_cart(request):
    cart_items = []
    subtotal = 0
    tax = 0
    total = 0
    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(user=request.user)
            order = Order.objects.get(owner=customer, order_status=Order.CART_STAGE, delete_status=Order.LIVE)
            cart_items = order.added_items.select_related('product').all()
            subtotal = sum(item.product.price * item.quantity for item in cart_items if item.product)
            tax = round(subtotal * 0.15, 2)  # 15% tax
            total = subtotal + tax
        except (Customer.DoesNotExist, Order.DoesNotExist):
            pass
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
    }
    return render(request, 'cart.html', context)

# Add item to cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    customer, _ = Customer.objects.get_or_create(user=request.user)

    # Get or create a cart (Order in CART_STAGE)
    order, _ = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE,
        delete_status=Order.LIVE
    )

    # Handle quantity from POST (form) or default to 1
    quantity = int(request.POST.get('quantity', 1))

    # Get or create the cart item
    item, created = OrderedItem.objects.get_or_create(owner=order, product=product)
    if created:
        item.quantity = quantity
    else:
        item.quantity += quantity
    item.save()

    return redirect('cart')

# Remove item from cart
@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderedItem, pk=item_id, owner__owner__user=request.user, owner__order_status=Order.CART_STAGE)
    item.delete()
    return redirect('cart')

# Confirm order
@login_required
def confirm_order(request):
    customer = get_object_or_404(Customer, user=request.user)
    try:
        order = Order.objects.get(owner=customer, order_status=Order.CART_STAGE, delete_status=Order.LIVE)
        order.order_status = Order.ORDER_CONFIRMED
        order.save()
    except Order.DoesNotExist:
        pass
    return redirect('cart')