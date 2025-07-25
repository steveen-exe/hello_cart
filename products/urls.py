from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_index'),
    path('products_list/', views.list_products, name='list_products'),
    path('product_detail/<int:pk>/', views.product_detail, name='detail_product')
]
