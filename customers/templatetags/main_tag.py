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
