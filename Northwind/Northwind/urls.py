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

from django.conf import settings
from django.conf.urls.static import static

# Import all your ViewSets
from categories.views import CategoryViewSet
from customers.views import CustomerViewSet
from employees.views import EmployeeViewSet, TerritoryViewSet, EmployeeTerritoryViewSet
from orders.views import OrderViewSet, OrderDetailViewSet
from products.views import ProductViewSet
from regions.views import RegionViewSet
from shippers.views import ShipperViewSet
from suppliers.views import SupplierViewSet
from dashboard.views import DashboardViewSet

router = DefaultRouter()

# Register all viewsets with explicit, unique basenames
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"customers", CustomerViewSet, basename="customer")
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"territories", TerritoryViewSet, basename="territory")
router.register(r"employeeterritories", EmployeeTerritoryViewSet, basename="employeeterritory")
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"orderdetails", OrderDetailViewSet, basename="orderdetail")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"regions", RegionViewSet, basename="region")
router.register(r"shippers", ShipperViewSet, basename="shipper")
router.register(r"suppliers", SupplierViewSet, basename="supplier")
router.register(r"dashboard", DashboardViewSet, basename="dashboard")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)