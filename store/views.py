from django.shortcuts import render
from .models import Products
from category.models import Category
from django.shortcuts import get_object_or_404

def store(request,category_slug=None):
    categoiries = None
    products = None

    if category_slug != None:
        categoiries = get_object_or_404(Category,slug=category_slug)
        products = Products.objects.filter(category=categoiries,is_available=True)  
    else:
        products = Products.objects.all().filter(is_available=True)

    products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count,
    }

    return render(request, 'store/store.html', context)