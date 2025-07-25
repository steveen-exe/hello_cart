import random
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

def index(request):
    all_products = list(Product.objects.all())

    # Shuffle for random selection
    random.shuffle(all_products)

    # Get any 4 products for featured
    featured_products = all_products[:4]

    # Get latest 4 based on created time
    latest_products = Product.objects.order_by('-created_at')[:4]

    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
    }
    return render(request, 'index.html', context)

def list_products(request):
    # Get page number from query string (?page=2)
    page_number = request.GET.get('page', 1)

    # Fetch all products and paginate
    product_list = Product.objects.order_by('-priority')
    paginator = Paginator(product_list, 4)  # 2 products per page
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj
    }
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context={
        'product' : product
    }
    return render(request, 'product_detail.html', context)
