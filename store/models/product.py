from django.db import models
from django.urls import reverse, reverse_lazy


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default="Product Description")
    price = models.PositiveIntegerField(default=100)
    image = models.URLField(
        default="https://www.electricmirror.com/wp-content/uploads/2022/05/image-coming-soon.jpg"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def get_absolute_url_for_add_to_basket(self):
        return reverse_lazy("item_add", kwargs={"pk": self.pk})

    def get_absolute_url_for_remove_from_basket(self):
        return reverse_lazy("item_remove", kwargs={"pk": self.pk})
    


