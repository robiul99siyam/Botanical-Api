from django.contrib import admin
from .models import OrderProduct
# Register your models here.


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class ProductOreder(admin.ModelAdmin):
    list_display = ['product_name','current_address','phone_number', 'product_dealybary']
    def save_model(self,request,obj,form,change):
        if obj.product_dealybary == 'Running':
            email_subject = "Tree Shop Order Now "
            email_body = render_to_string('oreder.html',{'user':obj.user})
            email = EmailMultiAlternatives(email_subject,'',to=[obj.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()


admin.site.register(OrderProduct,ProductOreder)
