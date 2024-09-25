from .models import Commandes, Produits
from typing import Any


def addProduit(id: int) -> int:
    try:
        produit_tps = Produits(id=id)
        produit_tps.save()

        return 1
    except Exception:
        return 0


def searchProduit(id: int) -> Any:
    try:
        produits = Produits.objects.all()
        produits = Produits.objects.filter(id=id)
        return produits

    except Exception:
        return 0


def deleteProduits(id: int) -> int:
    try:
        Produits.objects.filter(id=id).delete()
        return 1
    except Exception:
        return 0


def addCommande(customerId: int, products: str) -> int:
    try:
        commandes_tps = Commandes(customerId=customerId)
        for prod in products.split(','):
            p1 = Produits(id=int(prod))
            p1.save()
            commandes_tps.save()
            commandes_tps.products.add(p1)  
        print("banane")        
        commandes_tps.save()
        return 1
    except Exception:
        return 0


def updateCommande(id: int, customerId: int = 0, products: str = "") -> int:
    try:
        Commande = Commandes.objects.filter(id=id)[0]
        if customerId != 0:
            Commande.customerId = customerId
        if products != "":
            for prods in products :
                p1 = Produits(id=int(prods))
                Commande.products.add(p1)
        Commande.save()
        return 1
    except Exception:
        return 0


def searchCommande(id: int = 0, customerId: int = 0, products: int = 0) -> Any:
    try:
        commandes = Commandes.objects.all()
        if id != 0:
            print("allo", id)
            commandes = Commandes.objects.filter(id=id)
        else:
            if customerId != 0:
                commandes = Commandes.objects.filter(customerId=customerId)
            if products != 0:
                commandes = Commandes.objects.filter(products=products)
        return commandes

    except Exception:
        return 0


def getCommandes() -> Any:
    try:
        return Commandes.objects.all()

    except Exception:
        return 0


def deleteCommande(id: int) -> int:
    try:
        Commandes.objects.filter(id=id).delete()
        print("dbfunction : delete true")
        return 1
    except Exception:
        print("dbfunction : delete false")
        return 0
