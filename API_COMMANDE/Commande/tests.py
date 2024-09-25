from django.test import TestCase
from .models import Commandes, Produits
import Commande.DBFunctions as dbf


class ProduitsTestCase(TestCase):
    def setUp(self) -> None:
        self.p1 = Produits.objects.create(id=1)
        self.p2 = Produits.objects.create(id=2)

    def testCreateProduits(self) -> None:
        dbf.addProduit(id=3)
        self.assertEqual(Produits.objects.all().count(), 3)

    def testReadProduits(self) -> None:
        self.assertEqual(dbf.searchProduit(id=1).count(), 1)

    def testDeleteproduits(self) -> None:
        dbf.deleteCommande(id=3)
        self.assertEqual(Produits.objects.all().count(), 2)


class CommandesTestCase(TestCase):
    def setUp(self) -> None:
        self.produit1 = Produits.objects.create(id=1)
        self.produit2 = Produits.objects.create(id=2)
        self.commande1 = Commandes.objects.create(customerId=1)
        self.commande1.products.set([self.produit1])
        self.commande2 = Commandes.objects.create(customerId=1)
        self.commande2.products.set([self.produit1])

    def testCreateCommande(self) -> None:
        dbf.addCommande(customerId=2, products="1")
        self.assertEqual(Commandes.objects.all().count(), 3)

    def testReadCommande(self) -> None:
        self.assertEqual(dbf.searchCommande(customerId=1).count(), 2)

    def testUpdateCommande(self) -> None:
        dbf.updateCommande(id=2, customerId=3)
        self.assertEqual(dbf.searchCommande(id=0, customerId=3).count(), 1)

    def testDeleteCommande(self) -> None:
        dbf.deleteCommande(id=3)
        self.assertEqual(Commandes.objects.all().count(), 2)


