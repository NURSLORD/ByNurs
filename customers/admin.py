from django.contrib import admin

# Register your models here.
from customers.models import MyUser, Order, ItemOrders


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    list_display_links = list_display


class ItemOrderAdmin(admin.TabularInline):
    model = ItemOrders
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'address', 'total_item', 'ord_date']
    list_display_links = ['customer', 'address', 'ord_date']
    search_fields = ['invoice_number']
    inlines = [ItemOrderAdmin]

