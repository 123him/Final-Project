from django.db import models

# Create your models here.
class account(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=50)
    class Meta:
        db_table = "account"