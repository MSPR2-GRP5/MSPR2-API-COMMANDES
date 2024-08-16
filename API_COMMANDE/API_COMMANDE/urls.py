from typing import Any

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI,Schema
import Commande.DBFunctions as dbf
from datetime import datetime
# from ninja_apikey.security import APIKeyAuth

#api = NinjaAPI(auth=APIKeyAuth())
api = NinjaAPI()

class ProductSchema(Schema):
    id : int

class CommandesOut(Schema):
    id : int
    createdAt : datetime
    customerId : int
    products : ProductSchema
    
    

@api.post("")
def addCommande(request: Any, customerId: int, products: int) -> int:
    return dbf.addCommande(customerId, products)

@api.get("",response=list[CommandesOut])
def getCommandes(request : Any) -> Any:
    return dbf.getCommandes()


@api.delete("")
def deleteCommande(request: Any, id: int) -> int:
    print("url debug")
    return dbf.deleteCommande(id)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", api.urls),
]
