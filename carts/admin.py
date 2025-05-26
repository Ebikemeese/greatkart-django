from django.contrib import admin
from .models import Cart, cartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class cartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

# Register your models here.
admin.site.register(Cart, CartAdmin)
admin.site.register(cartItem, cartItemAdmin)