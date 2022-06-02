from multiprocessing import Condition
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

class Product(models.Model):
    pro_name = models.CharField(max_length=200)
    pro_des = models.CharField(max_length=2000)
    photo =  models.CharField(max_length=500)
    time_stamp = models.DateTimeField()
    deadline = models.DateTimeField()
    current_bid = models.FloatField()
    likes = models.IntegerField()
    views = models.IntegerField()
    selling_price = models.FloatField()
    condition = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Customer(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    mobile_number= models.IntegerField(max_length=10)
    address= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    username= models.CharField(max_length=200)
    password= models.CharField(max_length=200)

class Vendor(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    mobile_number= models.IntegerField(max_length=10)
    address= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    username= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    shop_name= models.CharField(max_length=200)

class Bids(models.Model):
    bid_amount= models.IntegerField(max_length=100)
    bid_time= models.DateTimeField()
    status_choices = (('Sold', 'Sold'),
        ('On Bid', 'On Bid'), 
        )
    status = models.CharField(max_length = 100, choices = status_choices, default="In Progress")
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
