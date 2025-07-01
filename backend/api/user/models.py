from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    img = models.ImageField(upload_to="user_images/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name