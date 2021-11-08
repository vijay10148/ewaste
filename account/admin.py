from django.contrib import admin
from .models import UserDetail,UserProduct,statusdata

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(UserProduct)
admin.site.register(statusdata)
