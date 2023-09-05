from django.db import models

# Create your models here.
class user_account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = "user_account"

class restaurant_account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    restaurant_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    type_of_restaurant = models.CharField(max_length=50)
    authirised_person = models.CharField(max_length=50)
    no_of_staff = models.IntegerField()
    photo = models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = "restaurant_account"

class offer(models.Model):
    restaurant_id=models.CharField(max_length=50)
    menu_item_name=models.CharField(max_length=50)
    offer=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    details=models.CharField(max_length=100)
    status=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)

    class Meta:
        db_table='offer'

class food_item(models.Model):
    restaurant_name=models.CharField(max_length=50)
    menu_name=models.CharField(max_length=50)
    menu_item_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField()
    type=models.CharField(max_length=50)
    cooking_time=models.TimeField()
    status=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)

    class Meta:
        db_table='food_item'

class food_menu(models.Model):
    restaurant_name=models.CharField(max_length=50)
    menu_name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    orgin=models.CharField(max_length=50)
   
    photo=models.CharField(max_length=500)

    class Meta:
        db_table='food_menu'

class tble_rest_admin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    restaurant_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    restaurant_id=models.CharField(max_length=50)
   

    class Meta:
        db_table='tble_rest_admin'

class tbl_feedback(models.Model):
    feedback_id=models.CharField(max_length=50)
    customer_id=models.CharField(max_length=50)
    feedback=models.CharField(max_length=50)
    status=models.IntegerField()
    
    class Meta:
        db_table='tbl_feedback'
