from django.db import models

# Create your models here.

class Produits(models.Model) :
    objects: models.Manager["Produits"]
    id = models.IntegerField(primary_key=True, null = False)


class Commandes(models.Model) :
    objects: models.Manager["Commandes"]
    createdAt = models.DateField()
    id = models.AutoField(primary_key=True,null=False)
    customerId = models.IntegerField(null = False)
    products = models.ManyToManyField(Produits)
