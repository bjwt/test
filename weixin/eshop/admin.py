from django.contrib import admin

from order.models import Order
from product.models import Product,Ptype
from eshopuser.models import UserProfile
admin.site.register(Product)
admin.site.register(Ptype)
admin.site.register(UserProfile)
admin.site.register(Order)