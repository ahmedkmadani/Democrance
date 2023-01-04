from django.urls import path, include
from rest_framework import routers
from app.views.customer import CustomerView


router = routers.DefaultRouter()
router.register(r"create_customer", CustomerView, basename="customer")

urlpatterns = [
    path("", include(router.urls)),
]
