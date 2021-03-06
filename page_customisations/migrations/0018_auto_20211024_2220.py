# Generated by Django 3.2.3 on 2021-10-24 21:20

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0017_auto_20211024_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='globalsitestyling',
            old_name='secondary_button_base_color',
            new_name='secondary_button_color',
        ),
        migrations.AddField(
            model_name='globalsitestyling',
            name='secondary_button_border',
            field=models.TextField(choices=[('action-button-border', 'Add Border'), ('no-border-action-button-border', 'No Border')], default='no-border-action-button-border'),
        ),
        migrations.AddField(
            model_name='globalsitestyling',
            name='secondary_button_border_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__center', 'Center'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__center', 'Center'), ('text-align__right', 'Right')], default='text-align__left'),
        ),
    ]
