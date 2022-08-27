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
            messages.success(request, 'Вы не авторизованы!')
            return redirect('my_login')
    context = {
        'title': 'Войти',
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True),
    }

    return render(request, 'user/login.html', context)


def set_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        full_name = request.POST["first_name"]
        phone = request.POST["phone"]
        if password != password2:
            messages.error(request, 'Пароли не правильные!')
            return redirect('my_register')
        user = User()
        user.username = username
        user.email = email
        user.password = password
        MyUser.objects.create(username=username, email=email, full_name=full_name, phone_number=phone)
        user.set_password(password)
        user.save()
        user1 = authenticate(username=username, password=password)
        if user1 is not None:
            login(request, user1)
        messages.success(request, 'Вы на сайте')
        return redirect('home')
    context = {
        'title': 'Регистация',
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True),
    }
    return render(request, "user/register.html", context)


def logout_my(request):
    if request.method == 'POST':
        logout(request)
    return redirect('my_login')


def set_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            image = request.FILES['image']
            full_name = request.POST['full_name']
            phone = request.POST['number_phone']
            email = request.POST['email']
            user = MyUser.objects.get(username=request.user.username)
            user.image = image
            user.email = email
            user.phone_number = phone
            user.full_name = full_name
            user.save()
        context = {
            'title': 'Редактировать',
            'cats': Category.objects.all(),
            "brand": Brand.objects.all().filter(is_active=True),
            'sells': Sell.objects.all().filter(is_active=True),
            'address': Address.objects.all().filter(is_active=True),
            'customer': MyUser.objects.get(username=request.user.username)

        }
        return render(request, 'user/edit.html', context=context)
    else:
        return redirect('my_login')


def wishlist_add(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        if int(pk) != 0:
            product = Product.objects.get(pk=pk)
            user.wishlist.add(product)
    else:
        return redirect('my_login')

    context = {
        'title': 'Избранные',
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
        'title': 'Избранные',
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
        id = product.sub_category.pk
        return redirect('shop', pk=id)
    else:
        return redirect('my_login')


def cart_delete(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        product = Product.objects.get(pk=pk)
        user.cart.remove(product)
    else:
        return redirect('my_login')
    user = MyUser.objects.get(username=request.user.username)
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
        'title': 'Избранные',
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, 'wishlist.html', context)
