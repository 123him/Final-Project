# Generated by Django 4.2.2 on 2023-09-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_rename_authirised_person_restaurant_account_authorised_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='end_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='offer',
            name='start_date',
            field=models.IntegerField(),
        ),
    ]
