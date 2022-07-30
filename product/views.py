from django.shortcuts import render

# Create your views here.
from customers.models import MyUser
from product.models import Category, SubCategory, Brand, Product
from shop.models import Sell, Address, Reclame


def set_index(request):
    context = {
        'title': 'Главная',
        'cats': Category.objects.all(),
        'sub_cat': SubCategory.objects.all().filter(is_active=True)[:6],
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True),
        'reclames': Reclame.objects.all()[:5],
        'products': Product.objects.all().order_by('pub_date')[:8]

    }

    return render(request, "index.html", context)


def set_shop(request, pk):
    if request.method == 'POST':
        word = request.POST['find_product']
        products = Product.objects.all().filter(title__icontains=word)
        title = word
    else:
        products = Product.objects.all().filter(sub_category=pk)
        title = (SubCategory.objects.get(pk=pk)).title

    context = {
        'title': title,
        'cats': Category.objects.all(),
        'product': products,
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "shop.html", context)


def set_shop_detail(request, pk):
    product = Product.objects.get(pk=pk)
    category = product.sub_category
    context = {
        'title': (SubCategory.objects.get(pk=pk)).title,
        'one_product': product,
        'products': Product.objects.filter(sub_category=category),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)

    }
    return render(request, "shop-detail.html", context)


def set_product(request):
    return render(request, "product.html")
