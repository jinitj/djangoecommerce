from django.contrib import admin
from store.models import Customer,Product,Cart,CartElement
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartElement)