# Generated by Django 4.2.6 on 2024-02-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_tag',
        ),
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.ManyToManyField(to='product.producttag'),
        ),
    ]
