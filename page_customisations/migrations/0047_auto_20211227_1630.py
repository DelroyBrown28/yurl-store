# Generated by Django 3.2.3 on 2021-12-27 16:30

from django.db import migrations, models
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0046_homepage_customisation_right_banner_image_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage_customisation',
            name='right_banner_image_3',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to='home_page_images'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__right', 'Right'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__right', 'Right'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
    ]
