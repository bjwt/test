#coding=UTF-8
from django.conf.urls import *

from models import *
from views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^query$', query),
)
