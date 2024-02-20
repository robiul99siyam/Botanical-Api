from django.db import models




class DailyProduct(models.Model):
    PRODUCT_SIZE = (
        ("L","L"),
        ("M","M"),
        ("S","S"),
        ("XL","XL"),
        ("XXL","XXL"),
    )
    image = models.ImageField(upload_to='Daily_product/media/images/')
    name = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=20,null=True)
    quentity = models.CharField(max_length=20,null=True)
    product_code  = models.CharField(max_length=20,null=True)
    Shopping_tex = models.CharField(max_length=20,null=True)
    size = models.CharField(max_length=20,choices=PRODUCT_SIZE,null=True)
    