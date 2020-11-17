from django.urls import include, path
from rest_framework import routers
from .views import EmployeeViewSet, CompanyViewSet, PartnershipViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'partnerships', PartnershipViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]