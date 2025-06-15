from django.db import models

# Create your models here.

class User(models.Model):
    first = models.CharField( max_length=50)
    last = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)
    image = models.ImageField( upload_to='image', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.user