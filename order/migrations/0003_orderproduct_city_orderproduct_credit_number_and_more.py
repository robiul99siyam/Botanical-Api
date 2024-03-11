# Generated by Django 4.2.6 on 2024-03-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderproduct_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='credit_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='zip_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
