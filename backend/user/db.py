import os
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
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

class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
    
    def set_password(self, raw_password):
        """Hash and set the user's password."""
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        """Verify the user's password."""
        return check_password(raw_password, self.password)
    
    def save_to_redis(self):
        """Save user data to Redis as a hash."""
        user_data = {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
        try:
            redis_client.hset(f"{settings.REDIS_PREFIX}:user:{self.user_id}", mapping=user_data)
        except redis.RedisError:
            pass

    def delete_from_redis(self):
        """Delete user data from Redis."""
        try:
            redis_client.delete(f"{settings.REDIS_PREFIX}:user:{self.user_id}")
        except redis.RedisError:
            pass
    
    def save(self, *args, **kwargs):
        """Override save method to save user data to Redis."""
        super().save(*args, **kwargs)
        self.save_to_redis()

    def delete(self, *args, **kwargs):
        """Override delete method to remove user data from Redis."""
        self.delete_from_redis()
        super().delete(*args, **kwargs)