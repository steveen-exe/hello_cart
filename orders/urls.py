from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.show_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/confirm/', views.confirm_order, name='confirm_order'),
]
