from django.db import models
from django.contrib.auth.models import User



class ProductTag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __str__(self) -> str:
        return self.name

    



class Product(models.Model):
    PRODUCT_SIZE = (
        ("L","L"),
        ("M","M"),
        ("S","S"),
        ("XL","XL"),
        ("XXL","XXL"),
    )
    image = models.ImageField(upload_to='product/media/images/')
    name = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=20,null=True)
    quentity = models.CharField(max_length=20,null=True)
    product_code  = models.CharField(max_length=20,null=True)
    Shopping_text = models.CharField(max_length=20,null=True)
    size = models.CharField(max_length=20,choices=PRODUCT_SIZE,null=True)
    product_tag = models.ManyToManyField(ProductTag)


    def __str__(self) -> str:
        return self.name


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


class reviewer(models.Model):
    reviewer = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices=STAR_CHOICES,max_length=20)

    

    