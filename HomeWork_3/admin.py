from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    ordering = ('name',)
    list_filter = ('registration_date',)

    fields = ('name', 'email', 'tel', 'address', 'registration_date',)
    readonly_fields = ('registration_date',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'count',)
    ordering = ('name',)
    list_filter = ('price', 'count',)
    search_fields = ('description',)

    fields = ('name', 'description', 'price', 'count', 'create_date',)
    readonly_fields = ('create_date',)


class ProductInOrderInline(admin.TabularInline):
    model = Order.products.through
    extra = 1
    fields = ('product', 'product_price', 'product_count')
    readonly_fields = ('product_price',)

    def product_price(self, instance):
        return instance.product.price


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'customer', 'total_amount', 'date',)
    ordering = ('customer',)
    list_filter = ('customer', 'products', 'total_amount', 'date',)

    fields = ('customer', 'date', 'total_amount',)
    readonly_fields = ('date', 'total_amount',)
    inlines = (ProductInOrderInline,)

    def save_related(self, request, form, formsets, change):
        super(OrderAdmin, self).save_related(request, form, formsets, change)
        form.instance.update_total()


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)