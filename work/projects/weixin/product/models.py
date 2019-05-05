#coding=UTF-8
from django.db import models


class Product(models.Model):
    name=models.CharField('product name',max_length=30)
    pric=models.FloatField('price',default=10)
    ptype=models.ForeignKey('Ptype')
    img=models.ImageField('img',upload_to='product',max_length=100)
    
    def __unicode__(self):
        return "%s ---> %f" %(self.name,self.pric)

class Ptype(models.Model):
    name=models.CharField('type',max_length=10)
    
    def __unicode__(self):
        return "%s" %self.name    