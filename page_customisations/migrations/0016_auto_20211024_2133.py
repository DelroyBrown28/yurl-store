# Generated by Django 3.2.3 on 2021-10-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0015_auto_20211024_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='globalsitestyling',
            old_name='primary_button_text_color',
            new_name='action_button_text_color',
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
    ]
