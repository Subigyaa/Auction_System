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

    