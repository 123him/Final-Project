# Generated by Django 4.2.2 on 2023-09-10 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_rename_restaurant_id_offer_restaurant_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='restaurant_name',
            new_name='restaurant_id',
        ),
    ]
