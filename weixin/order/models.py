#coding=UTF-8
from django.db import models
from django.contrib.auth.models import User
from product.models import Product,Ptype

class Order(models.Model):
    odate=models.DateTimeField('order date',auto_now=True)
    product=models.ForeignKey(Product)
    user=models.ForeignKey(User)
    


