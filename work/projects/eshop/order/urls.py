from django.conf.urls import *

from models import *
from views import buy,index,info

urlpatterns = patterns('',
    url(r'buy/(?P<oid>\d+)$', buy),
    url(r'index$', index),
    url(r'info/(?P<oid>\d+)$',info),
)
