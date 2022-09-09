from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default="Product Description")
    price = models.PositiveIntegerField(default=100)
