# Generated by Django 4.2.6 on 2023-10-09 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_rename_price_tbl_cart_total_price_tbl_cart_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_cart',
            old_name='total_price',
            new_name='price',
        ),
    ]
