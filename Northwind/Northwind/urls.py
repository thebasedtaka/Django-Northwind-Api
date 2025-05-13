"""
URL configuration for Northwind project.

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from categories.views import CategoryViewSet
from customers.views import CustomerViewSet
from employees.views import EmployeeViewSet
from employees.views import TerritoryViewSet
from employees.views import EmployeeTerritoryViewSet
from orders.views import OrderViewSet, OrderDetailViewSet
from products.views import ProductViewSet
from regions.views import RegionViewSet
from shippers.views import ShipperViewSet
from suppliers.views import SupplierViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"customers", CustomerViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"territories", TerritoryViewSet)
router.register(r"employeeterritories", EmployeeTerritoryViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"orderdetails", OrderDetailViewSet)
router.register(r"products", ProductViewSet)
router.register(r"regions", RegionViewSet)
router.register(r"shippers", ShipperViewSet)
router.register(r"suppliers", SupplierViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]