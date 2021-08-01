from django.contrib import admin

from .models import customer, message, products

admin.site.register(message)
admin.site.register(products)
admin.site.register(customer)