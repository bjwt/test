#coding=UTF-8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    SEX_CHOICES=(
        ('0',u'女'), 
        ('1',u'男'),        
    )
    user=models.OneToOneField(User)
    nickName=models.CharField(u'昵称',max_length=30)
    sex=models.CharField(u'性别',choices=SEX_CHOICES,default=1,max_length=1)
    address=models.CharField(u'地址',max_length=100,null=True)
