from django.db import models
from datetime import date
# Create your models here.


class Produits(models.Model):
    objects: models.Manager["Produits"]

    id = models.AutoField(primary_key=True, null=False)


class Commandes(models.Model):
    objects: models.Manager["Commandes"]

    createdAt = models.DateField(default=date.today)
    id = models.AutoField(primary_key=True, null=False)
    customerId = models.IntegerField(null=False,default=1)
    products = models.ForeignKey(Produits, on_delete=models.DO_NOTHING, null=True)
    
