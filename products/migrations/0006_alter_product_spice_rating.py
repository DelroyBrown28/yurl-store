# Generated by Django 3.2.3 on 2021-12-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211220_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='spice_rating',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
