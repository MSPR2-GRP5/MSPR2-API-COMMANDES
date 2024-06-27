from django.db import models
from datetime import date
# Create your models here.


class Produits(models.Model):
    objects: models.Manager["Produits"]

    _id = models.IntegerField(primary_key=True, null=False)


class Commandes(models.Model):
    objects: models.Manager["Commandes"]

    _createdAt = models.DateField(default=date.today)
    _id = models.AutoField(primary_key=True, null=False)
    _customerId = models.IntegerField(null=False)
    _products = models.ForeignKey(Produits, on_delete=models.DO_NOTHING, null=True)
