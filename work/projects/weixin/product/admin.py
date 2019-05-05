from django.contrib import admin

# Register your models here.
from eshopuser.models import UserProfile
from order.models import Order
from product.models import Product, Ptype

admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Ptype)
