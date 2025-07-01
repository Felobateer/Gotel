from django.db import models
from hotel.models import Hotel
from user.models import User

# Create your models here.
class Rating(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='ratings')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rating {self.rate} by {self.user.name} for {self.hotel.name}"