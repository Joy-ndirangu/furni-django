from django.contrib import admin

# import models
from .models import Sliders, Product, Staff, Contact,  Blog

# Register your models here.
admin.site.register(Sliders)
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Contact)
admin.site.register(Blog)

