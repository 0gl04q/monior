from django.contrib import admin

from apps.management.models import Order, Card


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('author', 'query', 'created', 'last_search')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
