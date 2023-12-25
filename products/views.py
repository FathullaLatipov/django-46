from django.shortcuts import render

from products.models import Category, ProductModel


def home_page(request):
    # Собираем все данные категории
    category_info = Category.objects.all()
    product_info = ProductModel.objects.all()
    context = {'categories': category_info, 'products': product_info}
    return render(request, 'index.html', context)

def product_page(request):
    # Собираем все данные категории
    category_info = Category.objects.all()
    product_info = ProductModel.objects.all()
    context = {'categories': category_info, 'products': product_info}
    return render(request, 'shop-grid.html', context)

def get_product_category_page(request, pk):
    categories = Category.objects.get(pk=pk)
    products = ProductModel.objects.filter(product_category=categories)

    context = {'categories': categories, 'products': products}
    return render(request, 'shop-grid.html', context)