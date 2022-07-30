"""MyNewShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from customers.views import set_wishlist
from shop.views import set_about, set_checkout, set_contact, set_my_account, set_service, \
    set_news, set_blog_detail, set_blog
from product.views import set_index, set_shop, set_shop_detail, set_product

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', set_index, name='home'),
                  path('about/', set_about, name='about'),
                  path('checkout/', set_checkout, name='checkout'),
                  path('product/', set_product, name='product'),
                  path('contact/', set_contact, name='contact'),
                  path('account/', set_my_account, name='account'),
                  path('service/', set_service, name='service'),
                  path('shop/<int:pk>', set_shop, name='shop'),
                  path('wishlist/', set_wishlist, name='wishlist'),
                  path('', include('customers.urls')),
                  path('shop_detail/<int:pk>/', set_shop_detail, name='shop_detail'),
                  path('news/', set_news, name='news'),
                  path('blog_detail/', set_blog_detail, name='blog_detail'),
                  path('blog/', set_blog, name='blog'),
                  url(r'^chaining/', include('smart_selects.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
