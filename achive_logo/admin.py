from django.contrib import admin
from .models import Achive_logo

class AchiveAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Achive_logo, AchiveAdmin)
