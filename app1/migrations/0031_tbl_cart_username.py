# Generated by Django 4.2.6 on 2023-10-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_rename_menu_name_tbl_order_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_cart',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
