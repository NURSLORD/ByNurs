from django import template
from customers.models import *

register = template.Library()


@register.inclusion_tag('tags/count_cart.html')
def counter_cart(username):
    user = MyUser.objects.get(username=username)
    count = user.cart.count()
    return {'count': count}


@register.inclusion_tag('tags/cart_all.html')
def cart_all(username):
    user = MyUser.objects.get(username=username)
    carts = user.cart.all()
    summa_carts = sum([i.old_price for i in user.cart.all()])
    return {'cart': carts, 'summa_carts': summa_carts}


@register.inclusion_tag('tags/photos.html')
def photo_user(username):
    user = MyUser.objects.get(username=username)
    user = user.image.url
    return {'photos': user}


@register.inclusion_tag('tags/full_name.html')
def name_user(username):
    user = MyUser.objects.get(username=username)
    user = user.full_name
    return {'full_name': user}


@register.inclusion_tag('tags/phone.html')
def phone(username):
    user = MyUser.objects.get(username=username)
    user = user.phone_number
    return {'phone': user}

@register.inclusion_tag('tags/email.html')
def email(username):
    user = MyUser.objects.get(username=username)
    user = user.email
    return {'email': user}
