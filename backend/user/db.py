import os
import redis
from decouple import config
from pymongo import MongoClient, ASCENDING
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Redis setup
redis_pool = redis.ConnectionPool(
    host=config('REDIS_HOST', default='localhost'),
    port=config('REDIS_PORT', default=6379, cast=int),
    db=config('REDIS_DB', default=0, cast=int),
    decode_responses=True,
)
redis_client = redis.Redis(connection_pool=redis_pool)
REDIS_PREFIX = config('REDIS_PREFIX', default='gotel')

# MongoDB setup
mongo_client = MongoClient(
    host=config('MONGO_HOST', default='localhost'),
    port=config('MONGO_PORT', default=27017, cast=int),
    username=config('MONGO_USER', default=None),
    password=config('MONGO_PASSWORD', default=None)
)
db = mongo_client[config('MONGO_DB', default='gotel_db')]
users_collection = db['users']
users_collection.create_index([('user_id', ASCENDING)], unique=True)
users_collection.create_index([('email', ASCENDING)], unique=True)

class User:
    def __init__(self, user_id, name, email, password, created_at=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at or datetime.utcnow()

    @staticmethod
    def from_dict(data):
        return User(
            user_id=data['user_id'],
            name=data['name'],
            email=data['email'],
            password=data['password'],
            created_at=data.get('created_at', datetime.utcnow())
        )

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)

    def save_to_mongo(self):
        user_data = {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at
        }
        users_collection.update_one(
            {'user_id': self.user_id},
            {'$set': user_data},
            upsert=True
        )

    def save_to_redis(self):
        user_data = {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
        try:
            redis_client.hset(f"{REDIS_PREFIX}:user:{self.user_id}", mapping=user_data)
        except redis.RedisError:
            pass

    def delete_from_mongo(self):
        users_collection.delete_one({'user_id': self.user_id})

    def delete_from_redis(self):
        try:
            redis_client.delete(f"{REDIS_PREFIX}:user:{self.user_id}")
        except redis.RedisError:
            pass

    def save(self):
        self.save_to_mongo()
        self.save_to_redis()

    def delete(self):
        self.delete_from_mongo()
        self.delete_from_redis()