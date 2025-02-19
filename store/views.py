from django.shortcuts import render
from .models import Products
from category.models import Category
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator

def store(request,category_slug=None):
    categoiries = None
    products = None

    if category_slug != None:
        categoiries = get_object_or_404(Category,slug=category_slug)
        products = Products.objects.filter(category=categoiries,is_available=True)  
        paginator = Paginator(products,6)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
    else:
        products = Products.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,6)
        page = request.GET.get('page')
        paged_product =paginator.get_page(page)

    products_count = products.count()


   
    context = {
        'products': paged_product,
        'products_count': products_count,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product' : single_product ,
    }
    return render(request, 'store/product_detail.html',context)