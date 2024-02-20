from django.contrib import admin
from .models import ProductTag,Product,reviewer

class ProductTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(ProductTag,ProductTagAdmin)

admin.site.register(Product)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name','body','created','rating']
admin.site.register(reviewer,ReviewAdmin)
