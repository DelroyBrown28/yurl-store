from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    fieldsets = (
        (None, {
            "fields": (
                'order_number',
            )
        }),
        ('Customer Details', {
            'classes': ('fieldset_titles',),
            'fields': (
                'full_name',
                'user_profile',
                'email',
                'phone_number',
            )
        }),
        ('Delivey Address', {
            'classes': ('fieldset_titles',),
            'fields': (
                'country',
                'street_address1',
                'street_address2',
                'town_or_city',
                'county',
                'postcode',
            )
        }),
        ('Order Details', {
            'classes': ('fieldset_titles',),
            'fields': (
                'date',
                'delivery_cost',
                'order_total',
                'grand_total',
                'stripe_pid',
            )
        }),
    )

    list_display = (
        'full_name',
        'date',
        'order_total',
        'delivery_cost',
        'grand_total',
        'order_number',
    )
    readonly_fields = (
        'full_name',
        'email',
        'phone_number',
        'date',
        'order_total',
        'user_profile',
        'delivery_cost',
        'grand_total',
        'order_number',
        'country',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
    )
    search_fields = [
        'full_name',
        'date',
        'order_number',
        'email',
        'phone_number',
    ]
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
