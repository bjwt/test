#coding=UTF-8
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from models import Product,Ptype
from django.core.paginator import Paginator
from django.template import RequestContext

import datetime

productaction=r'/?pid='
def index(request):
    action=productaction
    user=request.user
    #query all product
    products=Product.objects.all()
    
    pagenum=1
    if request.REQUEST.has_key('pid'):
        pagenum=request.REQUEST['pid']
        
    p=Paginator(products,3)
    page=p.page(pagenum)
    
    return render_to_response("index.html",locals(),context_instance=RequestContext(request))

def query(request):
    action=productaction
    pagenum=1
    if request.REQUEST.has_key('pid'):
        pagenum=request.REQUEST['pid']
    
    products=[]
    if request.POST.has_key('productname'):
        products=Product.objects.filter(name__contains=request.POST['productname'])
    else:
        products=Product.objects.all()
    
    p=Paginator(products,2)
    page=p.page(pagenum) 
    
    return render_to_response("index.html",locals(),context_instance=RequestContext(request))