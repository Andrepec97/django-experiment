from django.db import models
from uuid import uuid4


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
        ordering = ["name"]
        db_table = "ingredient"
