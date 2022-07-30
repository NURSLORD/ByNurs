from django.contrib import admin

# Register your models here.
from django.db.models import QuerySet

from product.models import  Brand, Category, SubCategory, Product


@admin.register(Brand)
class BrandUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', ]
    list_display_links = ['title', ]
    save_on_top = True
    list_filter = ['is_active', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']
    list_per_page = 20
    search_fields = ['description', 'title']
    save_on_top = True


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_display_links = list_display
    list_per_page = 20
    search_fields = list_display
    list_filter = ['is_active', ]
    save_on_top = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_category', 'category', 'status', 'cur', 'amount', 'brand',
                    'article', 'old_price', 'pub_date']
    list_display_links = ['title', 'article', 'category', 'sub_category']
    search_fields = ['title', 'sub_category', 'category', 'article']
    list_filter = ['sub_category', 'category', 'status', 'brand']
    list_per_page = 15
    list_editable = ['amount', 'cur']
    date_hierarchy = 'pub_date'
    save_on_top = True
    actions = ['set_dollar', 'set_rub', 'add_one']

    @admin.action(description='Изменит волюта на доллар')
    def set_dollar(self, request, qs: QuerySet):
        qs.update(cur=Product.USD)

    @admin.action(description='Изменит волюта на рубль')
    def set_rub(self, request, qs: QuerySet):
        qs.update(cur=Product.RUB)

    @admin.action(description='Добавить одно количество')
    def add_one(self, request, qs: QuerySet):
        for i in qs:
            i.amount += 1
            i.save()