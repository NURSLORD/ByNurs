from django.contrib import admin

# Register your models here.
from django.db.models import QuerySet

from shop.models import Sell, Reclame, Address, AboutUs, Team, Contact


@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'image', 'is_pub']
    list_display_links = ['title', 'is_pub']
    save_on_top = True
    list_filter = ['is_active', ]


@admin.register(Reclame)
class ReclameAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'image', 'is_pub']
    list_display_links = ['title', 'is_pub']
    save_on_top = True
    list_filter = ['is_active', ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'image', 'email', 'phone_number', 'is_pub']
    list_display_links = ['title', 'email', 'is_pub']
    save_on_top = True
    list_filter = ['is_active', ]


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', ]
    list_display_links = ['title', ]
    save_on_top = True
    list_filter = ['is_active', ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'image', 'site']
    list_display_links = ['name', 'position']
    search_fields = ['name', 'description', ]
    list_filter = ['position']
    actions = [
        'set_clone_model',
    ]

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email']
    list_per_page = 20
    save_on_top = True
    list_display_links = ['name', 'email']
    search_fields = list_display
