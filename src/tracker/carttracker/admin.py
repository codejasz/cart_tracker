from django.contrib import admin
from django.contrib.auth.models import User
from .models import Cart, Item

class ItemInline(admin.TabularInline):
    model = Item

class CartAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]

admin.site.register(Cart, CartAdmin)
admin.site.register(Item)
