from django.db import models


class CreatedAtAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class UpdatedAtAbstract(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedUpdatedAbstract(CreatedAtAbstract, UpdatedAtAbstract):
    class Meta:
        abstract = True
        ordering = ["-created_at"]
