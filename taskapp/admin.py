from django.contrib import admin

# Register your models here.
from .models import data,iplist
admin.site.register(data)
admin.site.register(iplist)