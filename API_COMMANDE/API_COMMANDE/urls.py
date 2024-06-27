"""
URL configuration for API_COMMANDE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from typing import Any

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
import Commande.DBFunctions as dbf

api = NinjaAPI()


@api.post("/addCommande")
def addCommande(request: Any, customerId: int, products: int) -> int:
    return dbf.addCommande(customerId, products)

@api.delete("/deleteCommnande")
def deleteCommande(request: Any, id: int) -> int:
    print("url debug")
    return dbf.deleteCommande(id)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
