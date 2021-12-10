from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product Images', {
            'classes': ('fieldset_titles',),
            'fields': (
                'main_product_image',
                'alternative_image_1',
                'alternative_image_2',)

        }),
        ('Product Information', {
            "fields": (
                'name',
                'category',
                'price',
                'description',
                'has_sizes',
                'in_stock',
                'is_active',
                'add_to_cta_banner',)
        }),
    )
    search_fields = [
        'name',
        'sku',
        'price',
    ]
    list_filter = (
        'name',
        'category',
    )
    list_display = (
        'name',
        'add_to_cta_banner',
        'category',
    )
    list_display_links = (
        'name',
    )
    list_editable = (
        'add_to_cta_banner',
        'category',
    )
    readonly_fields = (
        'created',
        'updated',
        'created_by',
    )
    ordering = ('name',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'url_name',
    )
    list_display_links = ('category_name',)
    prepopulated_fields = {"url_name": ["category_name"]}
    
        

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
