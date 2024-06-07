from django.db import models
from encrypted_model_fields.fields import EncryptedCharField, EncryptedDateField



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
    amount = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.name

class Payment(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="E-mail")
    city = models.CharField(verbose_name="City", max_length=40)
    stripe_id = models.CharField(
        verbose_name="Stripe ID",
        unique=True,
        max_length=50,
        blank=True,
        null=True
    )
    phone_number = EncryptedCharField(
        verbose_name="Phone number",
        max_length=15
    )
    date_of_birth = EncryptedDateField(
        verbose_name="Date of birth"
    )
    postal_code = EncryptedCharField(
        verbose_name="Postal code",
        max_length=10
    )
    address = EncryptedCharField(
        verbose_name="Address",
        max_length=255
    )