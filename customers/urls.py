from django.urls import path, include

from customers.views import logout_my, set_login, set_register, set_edit, wishlist_add, wishlist_delete, cart_add, \
    cart_delete, set_cart

urlpatterns = [
    path('logout/', logout_my, name='logout_my'),
    path('logining/', set_login, name='my_login'),
    path('register/', set_register, name='my_register'),
    path('edit/', set_edit, name='edit'),
    path('cart/', set_cart, name='cart'),
    path('wishlist_add/<int:pk>', wishlist_add, name='wish_add'),
    path('wishlist_delete/<int:pk>', wishlist_delete, name='wish_delete'),
    path('cart_add/<int:pk>', cart_add, name='cart_add'),
    path('cart_delete/<int:pk>', cart_delete, name='cart_delete'),
]
