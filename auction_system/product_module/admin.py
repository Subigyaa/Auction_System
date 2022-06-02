from django.contrib import admin

# Register your models here.

from .models import Category, Product, Customer, Vendor, Bids
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Bids)


