from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django import forms


class Category(models.Model):
    category_name = models.CharField(max_length=254, blank=False, null=False)
    url_name = models.SlugField(max_length=254, unique=True)
    category_image = models.ImageField(
        null=False, blank=False, default='', upload_to='category_images', help_text='This will be the category image')
    category_description = RichTextField(default='')

    class Meta:
        verbose_name = 'Categories'

    def __str__(self):
        return self.category_name

    def get_category_name(self):
        return self.category_name



class Product(models.Model):
    main_product_image = models.ImageField(
        null=False, blank=False, default='', upload_to='product_images', help_text='This will be the main image in the carousel.')
    alternative_image_1 = models.ImageField(
        null=True, blank=True, upload_to='product_images', help_text='This will be the first image in the carousel.')
    alternative_image_2 = models.ImageField(
        null=True, blank=True, upload_to='product_images', help_text='This will be the second image in the carousel.')
    category = models.ForeignKey(
        'Category', null=True, blank=True, help_text='Assign product to category', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_creator', null=True)

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    product_display_description = RichTextField(default='')
    spice_rating = models.CharField(max_length=1, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0')
    add_to_cta_banner = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.name
