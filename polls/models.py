from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
        
        
class Checkout(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    def __str__(self) -> str:
        return self.name
    
