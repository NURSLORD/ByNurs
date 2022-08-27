from django.shortcuts import render, redirect

# Create your views here.
from customers.models import MyUser, Order
from product.models import Category, SubCategory, Brand, Product
from shop.models import Sell, Address, Reclame, Blog


def set_index(request):
    context = {
        'title': 'Главная',
        'cats': Category.objects.all(),
        'sub_cat': SubCategory.objects.all().filter(is_active=True)[:6],
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True),
        'reclames': Reclame.objects.all()[:5],
        'blog': Blog.objects.all()[:3],
        'products': Product.objects.all().order_by('pub_date')[:8]

    }

    return render(request, "index.html", context)


def set_shop(request, pk):
    if request.method == 'POST':
        word = request.POST['find_product']
        products = Product.objects.all().filter(title__icontains=word)
        title = word
        sort = 'Поиск'
    else:
        products = Product.objects.all().filter(sub_category=pk)
        title = (SubCategory.objects.get(pk=pk)).title
        sort = 'Категория'

    context = {
        'title': title,
        'sort': sort,
        'cats': Category.objects.all(),
        'product': products,
        'count': products.count(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "shop.html", context)


def set_shop1(request, title):
    if request.method == 'POST':
        word = request.POST['find_product']
        products = Product.objects.all().filter(title__icontains=word)
        title1 = word
        sort = 'Поиск'
    else:
        products = Product.objects.all().filter(brand__title=title)
        title1 = title
        sort = 'Бренд'
    context = {
        'title': title1,
        'sort': sort,
        'count': products.count(),
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
    category1 = product.sub_category
    context = {
        'title': (SubCategory.objects.get(pk=category1.pk)).title,
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


def my_order(request):
    if request.user.is_authenticated:
        orders = Order.objects.all().filter(customer__username=request.user.username).order_by("-ord_date")
    else:
        return redirect("my_login")
    context = {
        'orders': orders,
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "user/my_orders.html", context)


