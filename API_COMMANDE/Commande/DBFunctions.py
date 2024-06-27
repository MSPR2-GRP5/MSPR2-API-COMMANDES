from .models import Commandes, Produits
from typing import Any


def addProduit(id: int) -> int:
    try:
        produit_tps = Produits(_id=id)
        produit_tps.save()

        return 1
    except Exception:
        return 0


def searchProduit(id: int) -> Any:
    try:
        produits = Produits.objects.all()
        produits = Produits.objects.filter(_id=id)
        return produits

    except Exception:
        return 0


def deleteProduits(id: int) -> int:
    try:
        Produits.objects.filter(_id=id).delete()
        return 1
    except Exception:
        return 0


def addCommande(customerId: int, products: int) -> int:
    try:
        p1 = Produits(_id=products)
        p1.save()
        commandes_tps = Commandes(_customerId=customerId, _products=p1)
        commandes_tps.save()

        return 1
    except Exception:
        return 0


def updateCommande(id: int, customerId: int = 0, products: int = 0) -> int:
    try:
        Commande = Commandes.objects.filter(_id=id)[0]
        if customerId != 0:
            Commande._customerId = customerId
        if products != 0:
            Commande._products = products
        Commande.save()
        return 1
    except Exception:
        return 0


def searchCommande(id: int = 0, customerId: int = 0, products: int = 0) -> Any:
    try:
        commandes = Commandes.objects.all()
        if id != 0:
            print("allo", id)
            commandes = Commandes.objects.filter(_id=id)
        else:
            if customerId != 0:
                commandes = Commandes.objects.filter(_customerId=customerId)
            if products != 0:
                commandes = Commandes.objects.filter(_products=products)
        return commandes

    except Exception:
        return 0


def deleteCommande(id: int) -> int:
    try:
        Commandes.objects.filter(_id=id).delete()
        print("dbfunction : delete true")
        return 1
    except Exception:
        print("dbfunction : delete false")
        return 0
    
