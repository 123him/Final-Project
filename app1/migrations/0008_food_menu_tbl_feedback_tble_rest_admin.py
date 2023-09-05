# Generated by Django 4.2.2 on 2023-09-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_food_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=50)),
                ('menu_name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('orgin', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'food_menu',
            },
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_id', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_feedback',
            },
        ),
        migrations.CreateModel(
            name='tble_rest_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('restaurant_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('restaurant_id', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tble_rest_admin',
            },
        ),
    ]
