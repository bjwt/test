#coding=UTF-8
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Order
from product.models import Product,Ptype
from eshopuser.models import UserProfile
from django.core.paginator import Paginator
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import datetime

@login_required
def index(request):
    action=r'index?pid='
    orders=[]
    if request.user:
        orders=Order.objects.filter(user__username=request.user.username)
        
    pagenum=1
    if request.REQUEST.has_key('pid'):
        pagenum=request.REQUEST['pid']
        
    p=Paginator(orders,3)
    page=p.page(pagenum)

    return render_to_response("orderindex.html",locals(),context_instance=RequestContext(request))    

@login_required
def buy(request,oid): 
    user=request.user
    submit=True

    try:
        product=Product.objects.get(id=oid)
        if product:    
                order=Order.objects.create(product=product,user=request.user)        
    except:
        return  HttpResponseRedirect("/")
 
    return render_to_response("order.html",locals(),context_instance=RequestContext(request))

@login_required
def info(request,oid):
    user=request.user
    try:
        order=Order.objects.get(id=oid)
    except: 
        return  HttpResponseRedirect("/")
      
    return render_to_response("order.html",locals())

