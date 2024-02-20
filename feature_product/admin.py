from django.contrib import admin
from .models import Featuere_product
# Register your models here.

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name','price','quentity','product_code','Shopping_text','size']
admin.site.register(Featuere_product,FeatureAdmin)

