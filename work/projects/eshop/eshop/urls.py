#coding=UTF-8
from django.conf.urls import patterns, include, url
from eshopuser.views import login_view,logout_view
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('product.urls')),
    url(r'^order', include('order.urls')),
    url(r'^accounts/login/$', login_view),
    url(r'^accounts/logout/$',logout_view),
    #url(r'^eshop/', include('eshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)


