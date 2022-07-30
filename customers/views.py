from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from customers.models import MyUser
from product.models import Category, Brand, Product
from shop.models import Address, Sell


def set_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You are successfully logged in!')
            return redirect('my_register')
        else:
            messages.success(request, 'You are not logged in!')
            return redirect('my_login')
    context = {
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }

    return render(request, 'user/login.html', context)


def set_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password != password2:
            messages.error(request, 'Passwords are not correct!')
            return redirect('my_register')
        user = User()
        user.username = username
        user.email = email
        MyUser.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'you are in the site')
        return redirect('my_register')
    context = {
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "user/register.html", context)


def logout_my(request):
    if request.method == 'POST':
        logout(request)
    return redirect('my_login')


def set_edit(request):
    return render(request, 'user/edit.html')


def wishlist_add(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        if int(pk) != 0:
            product = Product.objects.get(pk=pk)
            user.wishlist.add(product)
    else:
        return redirect('my_login')

    context = {
        'title': 'Wishlist',
        'wishlist': user.wishlist.all(),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }

    return render(request, 'wishlist.html', context)


def wishlist_delete(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        product = Product.objects.get(pk=pk)
        user.wishlist.remove(product)
    else:
        return redirect('my_login')
    context = {
        'title': 'Wishlist',
        'wishlist': user.wishlist.all(),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, 'wishlist.html', context)


def cart_add(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        product = Product.objects.get(pk=pk)
        user.cart.add(product)
        user.wishlist.remove(product)
    else:
        return redirect('my_login')

    user = MyUser.objects.get(username=request.user.username)
    wishlist_delete(request, pk)
    # context = {
    #     'title': 'Корзина',
    #     'count_cart': user.cart.count(),
    #     'cart_products': user.cart.all(),
    #     'summa_cart': sum([i.old_price for i in user.cart.all()]),
    #     'summa_products': sum([i.old_price for i in user.cart.all()]),
    #     'cats': Category.objects.all(),
    #     "brand": Brand.objects.all().filter(is_active=True),
    #     'sells': Sell.objects.all().filter(is_active=True),
    #     'address': Address.objects.all().filter(is_active=True)
    #
    # }

    return redirect('shop_detail', pk=pk)


def cart_delete(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        product = Product.objects.get(pk=pk)
        user.cart.remove(product)
    else:
        return redirect('my_login')
    context = {
        'title': 'Корзина',
        'count_cart': user.cart.count(),
        'cart_products': user.cart.all(),
        'summa_cart': sum([i.old_price for i in user.cart.all()]),
        'summa_products': sum([i.old_price for i in user.cart.all()]),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)

    }

    return render(request, 'cart.html', context)


def set_wishlist(request):
    context = {
        'title': 'Избранное',
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, 'wishlist.html', context)


def set_cart(request):
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        context = {
            'title': 'Корзина',
            'cart_products': user.cart.all(),
            'cats': Category.objects.all(),
            "brand": Brand.objects.all().filter(is_active=True),
            'sells': Sell.objects.all().filter(is_active=True),
            'address': Address.objects.all().filter(is_active=True)
        }
    else:
        context = {
            'title': 'Корзина',
            'cats': Category.objects.all(),
            "brand": Brand.objects.all().filter(is_active=True),
            'sells': Sell.objects.all().filter(is_active=True),
            'address': Address.objects.all().filter(is_active=True)

        }
    return render(request, "cart.html", context)
