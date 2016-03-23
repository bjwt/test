#!/usr/bin/env python
# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE","blog.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "eshop.settings"
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
