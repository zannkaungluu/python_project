from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    content = models.TextField(default=None)
    image = models.ImageField(default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    content = models.TextField(default=None)

class Detail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(default=None)
    dob = models.DateField(default=None)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(default=datetime.now)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField(default=None)
    order_date = models.DateTimeField(default=datetime.now)