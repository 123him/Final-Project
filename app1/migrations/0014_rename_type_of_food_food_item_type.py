# Generated by Django 4.2.2 on 2023-09-07 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_rename_type_food_item_type_of_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food_item',
            old_name='type_of_food',
            new_name='type',
        ),
    ]
