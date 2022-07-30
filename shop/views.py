from datetime import datetime
import requests
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from MyNewShop import settings
from product.models import Category, Brand
from shop.models import Sell, Team, Address, AboutUs


def set_about(request):
    team = {
        'abouts': AboutUs.objects.all()[:4],
        'about': 'active',
        'teams': Team.objects.all(),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "about.html", team)


def set_checkout(request):
    context = {
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "checkout.html", context)


def set_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

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
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "contact-us.html", context)


def set_my_account(request):
    context = {
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "my-account.html", context)


def set_service(request):
    context = {
        'about': AboutUs.objects.all(),
        'teams': Team.objects.all(),
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "service.html", context)


def set_news(request):
    context = {
        'cats': Category.objects.all(),
        "brand": Brand.objects.all().filter(is_active=True),
        'sells': Sell.objects.all().filter(is_active=True),
        'address': Address.objects.all().filter(is_active=True)
    }
    return render(request, "news_sells.html", context)


def set_blog_detail(request):
    return render(request, "blog_detail.html")


def set_blog(request):
    return render(request, "blogs.html")
