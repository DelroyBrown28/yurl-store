# Generated by Django 3.2.3 on 2021-12-27 16:28

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0045_auto_20211227_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage_customisation',
            name='right_banner_image_2',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to='home_page_images'),
        ),
    ]
