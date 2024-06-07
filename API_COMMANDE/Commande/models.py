from django.db import models

# Create your models here.
class Commande(models.Model):
    idCommande = models.BigAutoField(primary_key=True)
    idClient = models.IntegerField(default=0)
