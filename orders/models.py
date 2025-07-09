from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_STATUS = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )

    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4

    STATUS_CHOICES = (
        (CART_STAGE, "CART_STAGE"),
        (ORDER_CONFIRMED, "ORDER_CONFIRMED"),
        (ORDER_PROCESSED, "ORDER_PROCESSED"),
        (ORDER_DELIVERED, "ORDER_DELIVERED"),
        (ORDER_REJECTED, "ORDER_REJECTED"),
    )

    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_STATUS, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Order #{self.pk} by {self.owner}"

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='added_cart')
    quantity = models.IntegerField(default=1)  # ⬅️ typo: was 'quality'
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')

    def __str__(self):
        return f"{self.quantity} x {self.product} in Order #{self.owner_id}"
