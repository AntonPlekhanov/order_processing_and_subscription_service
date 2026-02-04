from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=50)
    telegram_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Custom user'
        verbose_name_plural = 'Custom users'


class Tariff(models.Model):
    name = models.CharField(max_length=60)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=CASCADE)
    tariff = models.ForeignKey(Tariff, related_name='usersubscriptions', on_delete=models.PROTECT)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} {self.tariff}'









