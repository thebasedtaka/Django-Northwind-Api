from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DashboardViewSet

router = DefaultRouter()
router.register(r'dashboard', DashboardViewSet, basename='dashboard-stats')

urlpatterns = [
    path('/', include(router.urls)),
]