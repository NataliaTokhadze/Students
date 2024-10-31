from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    bio = models.TextField()
    date = models.DateField()
    age = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    dis = models.TextField()
    price = models.DecimalField(max_digits=30, decimal_places=2)
    count = models.CharField(max_length=30)
    storage = models.BooleanField(default=True)
    quantity = models.IntegerField(default=10)