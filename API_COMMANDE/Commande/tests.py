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
        self.commande1 = Commandes.objects.create(customerId=1, products=self.produit1)
        self.commande2 = Commandes.objects.create(customerId=1, products=self.produit2)


    def testCreateCommande(self) -> None:
        dbf.addCommande(customerId=2, products=1)
        self.assertEqual(Commandes.objects.all().count(), 3)

    def testReadCommande(self) -> None:
        self.assertEqual(dbf.searchCommande(customerId=1).count(), 2)

    def testUpdateCommande(self) -> None:
        dbf.updateCommande(id=2, customerId=3)
        self.assertEqual(dbf.searchCommande(id=0, customerId=3).count(), 1)

    def testDeleteCommande(self) -> None:
        dbf.deleteCommande(id=3)
        self.assertEqual(Commandes.objects.all().count(), 2)


# class ModelTests(TestCase):
#     def testmanytomanyrelation(self):

#         # Créez des instances de vos modèles
#         produit1 = Produits.objects.create(id=1)
#         produit2 = Produits.objects.create(id=2)
#         commande = Commandes.objects.create(customerId=1)

#         # Ajoutez les instances de Topping à la relation ManyToMany
#         commande.products.add(produit1, produit2)

#         # Vérifiez que la relation ManyToMany fonctionne correctement
#         self.assertEqual(commande.products.count(), 2)
#         self.assertTrue(produit1 in commande.products.all())
#         self.assertTrue(produit2 in commande.products.all())
