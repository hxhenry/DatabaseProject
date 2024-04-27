# Create your models here.

from django.db import models


class Account(models.Model):
    ANO = models.PositiveBigIntegerField(unique=True, max_length=20)
    ANAME = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ANO} - {self.ANAME}"


class Customer(models.Model):
    CUSFNAME = models.CharField(max_length=20)
    CUSLNAME = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.CUSFNAME} {self.CUSLNAME}"

