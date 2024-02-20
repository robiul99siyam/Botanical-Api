from django.db import models

# Create your models here.
class Achive_logo(models.Model):
    image = models.ImageField(upload_to='achive_logo/media/image/')
