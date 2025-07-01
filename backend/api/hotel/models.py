from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.TextField()
    email = models.EmailField(unique=True)
    website = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to="hotel_images/", blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name