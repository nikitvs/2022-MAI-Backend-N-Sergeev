from django.db import models
from category.models import Category

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['title']