# Generated by Django 3.2.3 on 2021-10-24 20:36

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0016_auto_20211024_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsitestyling',
            name='action_button_text_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
    ]
