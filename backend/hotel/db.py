import os
from django.db import models
from django.conf import settings
import redis
from decouple import config

redis_pool = redis.ConnectionPool(
    host=config('REDIS_HOST', default='localhost'),
    port=config('REDIS_PORT', default=6379, cast=int),
    db=config('REDIS_DB', default=0, cast=int),
    decode_responses=True,
)
redis_client = redis.Redis(connection_pool=redis_pool)

class Hotel(models.Model):
    hotel_id = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    website = models.URLField(max_length=255)
    img = models.FileField(upload_to='hotel_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=1, decimal_places=2)

    class Meta:
        db_table = 'hotels'
        unique_together = ('hotel_id', 'name')
    
    def save_to_redis(self):
        """Save hotel data to Redis as a hash."""
        hotel_data = {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'img': self.img.url if self.img else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'description': self.description,
            'price': str(self.price),
            'rating': str(self.rating)
        }
        try:
            redis_client.hset(f"{settings.REDIS_PREFIX}:hotel:{self.hotel_id}", mapping=hotel_data)
        except redis.RedisError:
            pass

    def delete_from_redis(self):
        """Delete hotel data from Redis."""
        try:
            redis_client.delete(f"{settings.REDIS_PREFIX}:hotel:{self.hotel_id}")
        except redis.RedisError:
            pass
    
    def save(self, *args, **kwargs):
        """Override save method to save hotel data to Redis."""
        super().save(*args, **kwargs)
        self.save_to_redis()

    def delete(self, *args, **kwargs):
        """Override delete method to remove hotel data from Redis."""
        self.delete_from_redis()
        super().delete(*args, **kwargs)
    