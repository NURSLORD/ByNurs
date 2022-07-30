from django.contrib import admin

# Register your models here.
from customers.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    list_display_links = list_display
