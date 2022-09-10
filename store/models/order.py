from django.db import models

from store.models.abstract import CreatedUpdatedAbstract


class Order(CreatedUpdatedAbstract):
    items = models.ManyToManyField("store.Item", related_name='items')

    def __str__(self):
        return f"{self.id} - order"