from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from subscriptions.models import CustomUser


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.CharField(max_length=160)
    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=160)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product





