from django.shortcuts import render

from products.models import Category, ProductModel


def home_page(request):
    # Собираем все данные категории
    category_info = Category.objects.all()
    product_info = ProductModel.objects.all()
    context = {'categories': category_info, 'products': product_info}
    return render(request, 'index.html', context)
