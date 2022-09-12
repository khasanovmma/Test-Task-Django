import email
from django.db import models

from store.models.abstract import CreatedAtAbstract


class Order(CreatedAtAbstract):
    items = models.ManyToManyField("store.Item", related_name='items', blank=True)
    ordered_by =  models.CharField(max_length=120, null=True)
    email = models.EmailField(null=True)
    session_id = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.id} - order"