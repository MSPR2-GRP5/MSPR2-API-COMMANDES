from Commandes.models import Commandes
from typing import Any

def addCommande(id: int, customerId: int, panierId: int) -> int:
    try:
        Commandes(id=id, customerId=customerId, panierId=panierId).save()
        return 1
    except Exception:
        return 0


def updateCommande(id: int, customerId: int = 0, panierId: int = 0) -> int:
    try:
        Commande = Commandes.objects.filter(id=id)[0]
        if customerId != 0:
            Commande.customerId = customerId
        if panierId != 0:
            Commande.panierId = panierId
        Commande.save()
        return 1
    except Exception:
        return 0

def searchCommande(id: int = 0, customerId: int = 0, panierId: int = 0) -> Any:
    try:
        Commandes = Commandes.objects.all()
        print("banane")
        if id != 0:
            print("allo", id)
            Commandes = Commandes.filter(id=id)
        else:
            if customerId != 0:
                Commandes = Commandes.filter(customerId=customerId)
            if panierId != 0:
                Commandes = Commandes.filter(panierId=panierId)
        return Commandes

    except Exception:
        return 0


def deleteCommande(id: int) -> int:
    try:
        Commandes.objects.filter(id=id).delete()
        return 1
    except Exception:
        return 0
