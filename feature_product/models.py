from django.db import models




class Featuere_product(models.Model):
    PRODUCT_SIZE = (
        ("L","L"),
        ("M","M"),
        ("S","S"),
        ("XL","XL"),
        ("XXL","XXL"),
    )
    image = models.ImageField(upload_to='feature_product/media/images/')
    name = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=20,null=True)
    quentity = models.CharField(max_length=20,null=True)
    product_code  = models.CharField(max_length=20,null=True)
    Shopping_text = models.CharField(max_length=20,null=True)
    size = models.CharField(max_length=20,choices=PRODUCT_SIZE,null=True)
    