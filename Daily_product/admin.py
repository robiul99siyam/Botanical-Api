from django.contrib import admin
from .models import DailyProduct
# Register your models here.

class DailyAdmin(admin.ModelAdmin):
    list_display = ['name','price','quentity','product_code','Shopping_tex','size']
admin.site.register(DailyProduct,DailyAdmin)
