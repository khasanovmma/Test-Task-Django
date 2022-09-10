from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default="Product Description")
    price = models.PositiveIntegerField(default=100)
    image = models.URLField(
        default="https://www.electricmirror.com/wp-content/uploads/2022/05/image-coming-soon.jpg"
    )

