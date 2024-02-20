from django.db import models

# Create your models here.
class BennerSection(models.Model):
    image = models.ImageField(upload_to="benner/media/image/")
    
    def __str__(self) -> str:
        return self.image