# Generated by Django 3.2.3 on 2021-12-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211220_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='all_products_description',
        ),
        migrations.AddField(
            model_name='product',
            name='spice_rating',
            field=models.IntegerField(default='1'),
        ),
    ]
