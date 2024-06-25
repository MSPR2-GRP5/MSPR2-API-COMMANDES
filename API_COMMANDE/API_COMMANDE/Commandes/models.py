from django.db import models

class Produits(models.Model) :
    objects: models.Manager["Produits"]
    id = models.CharField(max_length = 255, null = False)
    
class Commande(models.Model) :
    objects: models.Manager["Commande"]
    createdAt = models.DateField()
    id = models.AutoField(primary_key=True,null=False)
    customerId = models.CharField(max_length = 255, null = False)
    products = models.ManyToManyField(Produits)


    