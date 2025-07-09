from django.shortcuts import render

def index(request):
    return render(request ,'index.html')
def list_products(request):
    #return product list page
    return render(request ,'product_list.html')

def product_detail(request):
    return render(request ,'product_detail.html') 