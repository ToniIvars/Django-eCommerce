from django.contrib import admin
from .models import Product, Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'buyer', 'status')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)