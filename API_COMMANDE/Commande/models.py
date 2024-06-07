from django.db import models
from ninja import NinjaAPI, Schema

api =NinjaAPI()


# Create your models here.
class Commande(models.Model):
    idCommande = models.BigAutoField(primary_key=True)
    idClient = models.IntegerField(default=0)
    idProduit = models.IntegerField(default=0)
    dateCommande = models.TimeField("date d'achat")
    quantite = models.IntegerField(default=1)
    prix = models.IntegerField(default=0)

class HelloSchema(Schema):
    name: str = "world"

@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"