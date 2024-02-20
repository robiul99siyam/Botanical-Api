from django.db import models
from product.models import Product
from django.contrib.auth.models import User 

PRODUCT_DEALYBARY = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
class OrderProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_dealybary = models.CharField(max_length=40,choices=PRODUCT_DEALYBARY,default='Pending')
    product_name=models.CharField(max_length=40)
    current_address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    cencal = models.BooleanField(default=False)



